from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import List, Dict
import json
from datetime import datetime
from auth import get_current_user
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/ws", tags=["websocket"])


class ConnectionManager:
    """Manage WebSocket connections"""
    
    def __init__(self):
        # Store active connections: {user_id: [websocket1, websocket2, ...]}
        self.active_connections: Dict[int, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, user_id: int):
        """Accept and store a WebSocket connection"""
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)
    
    def disconnect(self, websocket: WebSocket, user_id: int):
        """Remove a WebSocket connection"""
        if user_id in self.active_connections:
            if websocket in self.active_connections[user_id]:
                self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
    
    async def send_personal_message(self, message: dict, user_id: int):
        """Send a message to a specific user (all their connections)"""
        if user_id in self.active_connections:
            disconnected = []
            for websocket in self.active_connections[user_id]:
                try:
                    await websocket.send_json(message)
                except:
                    disconnected.append(websocket)
            
            # Clean up disconnected sockets
            for ws in disconnected:
                self.disconnect(ws, user_id)
    
    async def broadcast_to_followers(self, message: dict, user_id: int, db: Session):
        """Send a message to all followers of a user"""
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            for follower in user.followers:
                await self.send_personal_message(message, follower.id)
    
    async def broadcast(self, message: dict):
        """Broadcast a message to all connected users"""
        for user_id in list(self.active_connections.keys()):
            await self.send_personal_message(message, user_id)


manager = ConnectionManager()


@router.websocket("/notifications")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str,
    db: Session = Depends(get_db)
):
    """
    WebSocket endpoint for real-time notifications
    Connect with: ws://localhost:8000/ws/notifications?token=YOUR_JWT_TOKEN
    """
    try:
        # Authenticate user from token
        # Note: We need to manually validate the token since WebSocket doesn't support Depends for auth
        from jose import jwt, JWTError
        from auth import SECRET_KEY, ALGORITHM
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                await websocket.close(code=1008, reason="Invalid token")
                return
        except JWTError:
            await websocket.close(code=1008, reason="Invalid token")
            return
        
        user = db.query(models.User).filter(models.User.username == username).first()
        if not user:
            await websocket.close(code=1008, reason="User not found")
            return
        
        # Connect the user
        await manager.connect(websocket, user.id)
        
        # Send welcome message
        await websocket.send_json({
            "type": "connection_established",
            "data": {
                "message": f"Welcome @{user.username}! You are now connected.",
                "user_id": user.id
            },
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Keep connection alive and handle incoming messages
        while True:
            data = await websocket.receive_text()
            
            # Parse incoming message
            try:
                message = json.loads(data)
                message_type = message.get("type", "unknown")
                
                # Handle different message types
                if message_type == "ping":
                    await websocket.send_json({
                        "type": "pong",
                        "timestamp": datetime.utcnow().isoformat()
                    })
                
                elif message_type == "broadcast":
                    # Broadcast to all followers
                    await manager.broadcast_to_followers(
                        {
                            "type": "user_message",
                            "data": {
                                "from": user.username,
                                "message": message.get("message", "")
                            },
                            "timestamp": datetime.utcnow().isoformat()
                        },
                        user.id,
                        db
                    )
                
                else:
                    # Echo back unknown messages
                    await websocket.send_json({
                        "type": "echo",
                        "data": message,
                        "timestamp": datetime.utcnow().isoformat()
                    })
            
            except json.JSONDecodeError:
                await websocket.send_json({
                    "type": "error",
                    "data": {"message": "Invalid JSON"},
                    "timestamp": datetime.utcnow().isoformat()
                })
    
    except WebSocketDisconnect:
        manager.disconnect(websocket, user.id)
        print(f"User {user.username} disconnected")
    
    except Exception as e:
        print(f"WebSocket error: {e}")
        manager.disconnect(websocket, user.id)


# Helper functions to send notifications (can be called from other routers)
async def notify_new_tweet(tweet_id: int, author_id: int, db: Session):
    """Notify followers when a new tweet is posted"""
    await manager.broadcast_to_followers(
        {
            "type": "new_tweet",
            "data": {
                "tweet_id": tweet_id,
                "author_id": author_id
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        author_id,
        db
    )


async def notify_new_like(tweet_id: int, liker_id: int, tweet_author_id: int):
    """Notify tweet author when someone likes their tweet"""
    await manager.send_personal_message(
        {
            "type": "new_like",
            "data": {
                "tweet_id": tweet_id,
                "liker_id": liker_id
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        tweet_author_id
    )


async def notify_new_follow(follower_id: int, followed_id: int):
    """Notify user when someone follows them"""
    await manager.send_personal_message(
        {
            "type": "new_follow",
            "data": {
                "follower_id": follower_id
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        followed_id
    )


async def notify_new_reply(tweet_id: int, reply_id: int, replier_id: int, original_author_id: int):
    """Notify original tweet author when someone replies"""
    await manager.send_personal_message(
        {
            "type": "new_reply",
            "data": {
                "original_tweet_id": tweet_id,
                "reply_id": reply_id,
                "replier_id": replier_id
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        original_author_id
    )
