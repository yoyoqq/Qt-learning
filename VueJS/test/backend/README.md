# Twitter Clone FastAPI

A comprehensive Twitter-like REST API built with FastAPI featuring:

## Features

### 🔐 Authentication & Authorization
- JWT-based authentication
- Secure password hashing with bcrypt
- Token-based access control
- Protected endpoints

### 👥 User Management
- **CREATE**: Register new users
- **READ**: Get user profiles, list users, view followers/following
- **UPDATE**: Update user profile (name, bio, email, password)
- **DELETE**: Delete user account
- Follow/Unfollow functionality

### 🐦 Tweet Operations
- **CREATE**: Post new tweets, reply to tweets, retweet
- **READ**: View tweets, get timeline, list user tweets, get replies
- **UPDATE**: Edit own tweets
- **DELETE**: Delete own tweets
- Like/Unlike tweets
- Personalized timeline based on followed users

### 🔴 Real-time Features (WebSocket)
- Live notifications for:
  - New tweets from followed users
  - New likes on your tweets
  - New followers
  - New replies to your tweets
- Real-time updates without polling

## API Endpoints

### Authentication (`/auth`)
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login with form-data
- `POST /auth/login/json` - Login with JSON body

### Users (`/users`)
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update current user
- `DELETE /users/me` - Delete current user
- `GET /users/{username}` - Get user by username
- `GET /users/` - List all users (paginated)
- `POST /users/{username}/follow` - Follow a user
- `DELETE /users/{username}/follow` - Unfollow a user
- `GET /users/{username}/followers` - Get user's followers
- `GET /users/{username}/following` - Get users followed by user

### Tweets (`/tweets`)
- `POST /tweets/` - Create new tweet
- `GET /tweets/` - List all tweets (public feed)
- `GET /tweets/timeline` - Get personalized timeline
- `GET /tweets/{tweet_id}` - Get specific tweet
- `PUT /tweets/{tweet_id}` - Update tweet (author only)
- `DELETE /tweets/{tweet_id}` - Delete tweet (author only)
- `POST /tweets/{tweet_id}/like` - Like a tweet
- `DELETE /tweets/{tweet_id}/like` - Unlike a tweet
- `GET /tweets/{tweet_id}/replies` - Get tweet replies
- `GET /tweets/user/{username}` - Get user's tweets

### WebSocket (`/ws`)
- `WS /ws/notifications?token=<JWT_TOKEN>` - Real-time notifications

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Documentation

Once running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Database

Uses SQLite by default (`twitter.db`). To use PostgreSQL, update the `SQLALCHEMY_DATABASE_URL` in `database.py`:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## WebSocket Connection

Connect to WebSocket for real-time updates:

```javascript
const token = "your-jwt-token";
const ws = new WebSocket(`ws://localhost:8000/ws/notifications?token=${token}`);

ws.onmessage = (event) => {
    const notification = JSON.parse(event.data);
    console.log(notification);
};
```

## Request Types Supported

- **GET** - Read operations
- **POST** - Create operations
- **PUT** - Update operations
- **DELETE** - Delete operations
- **WebSocket** - Real-time bidirectional communication

## Security

- Passwords are hashed using bcrypt
- JWT tokens for authentication
- Protected endpoints require valid tokens
- CORS enabled (configure for production)

## Models

### User
- id, username, email, password
- full_name, bio
- is_active, is_verified
- followers, following relationships

### Tweet
- id, content
- author, timestamps
- reply_to, retweet_of (for threading)
- likes relationship

## Example Usage

### 1. Register a user
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secret123",
    "full_name": "John Doe"
  }'
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=secret123"
```

### 3. Create a tweet
```bash
curl -X POST "http://localhost:8000/tweets/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello Twitter!"}'
```

## Project Structure

```
backend/
├── main.py              # FastAPI app initialization
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── database.py          # Database configuration
├── auth.py              # Authentication utilities
├── requirements.txt     # Python dependencies
└── routers/
    ├── auth_router.py   # Authentication endpoints
    ├── users.py         # User management endpoints
    ├── tweets.py        # Tweet operations endpoints
    └── websocket.py     # WebSocket real-time features
```
