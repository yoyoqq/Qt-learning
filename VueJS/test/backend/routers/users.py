from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from auth import get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=schemas.User)
def read_current_user(current_user: models.User = Depends(get_current_active_user)):
    """Get current user profile"""
    user_dict = schemas.User.model_validate(current_user).model_dump()
    user_dict['followers_count'] = len(current_user.followers)
    user_dict['following_count'] = len(current_user.following)
    user_dict['tweets_count'] = len(current_user.tweets)
    return user_dict


@router.put("/me", response_model=schemas.User)
def update_current_user(
    user_update: schemas.UserUpdate,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update current user profile"""
    from auth import get_password_hash
    
    update_data = user_update.model_dump(exclude_unset=True)
    
    # Hash password if provided
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    
    for field, value in update_data.items():
        setattr(current_user, field, value)
    
    db.commit()
    db.refresh(current_user)
    
    user_dict = schemas.User.model_validate(current_user).model_dump()
    user_dict['followers_count'] = len(current_user.followers)
    user_dict['following_count'] = len(current_user.following)
    user_dict['tweets_count'] = len(current_user.tweets)
    return user_dict


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_current_user(
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete current user account"""
    db.delete(current_user)
    db.commit()
    return None


@router.get("/{username}", response_model=schemas.UserProfile)
def get_user_by_username(
    username: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """Get user profile by username"""
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user_dict = schemas.User.model_validate(user).model_dump()
    user_dict['followers_count'] = len(user.followers)
    user_dict['following_count'] = len(user.following)
    user_dict['tweets_count'] = len(user.tweets)
    return user_dict


@router.get("/", response_model=List[schemas.User])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """List all users with pagination"""
    users = db.query(models.User).offset(skip).limit(limit).all()
    
    result = []
    for user in users:
        user_dict = schemas.User.model_validate(user).model_dump()
        user_dict['followers_count'] = len(user.followers)
        user_dict['following_count'] = len(user.following)
        user_dict['tweets_count'] = len(user.tweets)
        result.append(user_dict)
    
    return result


@router.post("/{username}/follow", response_model=schemas.FollowResponse)
def follow_user(
    username: str,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Follow a user"""
    user_to_follow = db.query(models.User).filter(
        models.User.username == username
    ).first()
    
    if not user_to_follow:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if user_to_follow.id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot follow yourself"
        )
    
    if user_to_follow in current_user.following:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already following this user"
        )
    
    current_user.following.append(user_to_follow)
    db.commit()
    
    return {
        "message": f"Successfully followed @{username}",
        "is_following": True
    }


@router.delete("/{username}/follow", response_model=schemas.FollowResponse)
def unfollow_user(
    username: str,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Unfollow a user"""
    user_to_unfollow = db.query(models.User).filter(
        models.User.username == username
    ).first()
    
    if not user_to_unfollow:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if user_to_unfollow not in current_user.following:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not following this user"
        )
    
    current_user.following.remove(user_to_unfollow)
    db.commit()
    
    return {
        "message": f"Successfully unfollowed @{username}",
        "is_following": False
    }


@router.get("/{username}/followers", response_model=List[schemas.User])
def get_user_followers(
    username: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """Get list of user's followers"""
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    followers = user.followers[skip:skip + limit]
    result = []
    for follower in followers:
        user_dict = schemas.User.model_validate(follower).model_dump()
        user_dict['followers_count'] = len(follower.followers)
        user_dict['following_count'] = len(follower.following)
        user_dict['tweets_count'] = len(follower.tweets)
        result.append(user_dict)
    
    return result


@router.get("/{username}/following", response_model=List[schemas.User])
def get_user_following(
    username: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """Get list of users that this user follows"""
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    following = user.following[skip:skip + limit]
    result = []
    for followed_user in following:
        user_dict = schemas.User.model_validate(followed_user).model_dump()
        user_dict['followers_count'] = len(followed_user.followers)
        user_dict['following_count'] = len(followed_user.following)
        user_dict['tweets_count'] = len(followed_user.tweets)
        result.append(user_dict)
    
    return result
