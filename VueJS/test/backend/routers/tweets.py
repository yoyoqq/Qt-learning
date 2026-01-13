from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
import models
import schemas
from database import get_db
from auth import get_current_active_user

router = APIRouter(prefix="/tweets", tags=["tweets"])


def _tweet_to_dict(tweet: models.Tweet, current_user: models.User) -> dict:
    """Convert tweet model to dict with additional fields"""
    tweet_dict = schemas.TweetWithAuthor.model_validate(tweet).model_dump()
    tweet_dict['likes_count'] = len(tweet.liked_by)
    tweet_dict['replies_count'] = len(tweet.replies)
    tweet_dict['retweets_count'] = len(tweet.retweets)
    tweet_dict['is_liked'] = current_user in tweet.liked_by
    
    # Add author info
    author_dict = schemas.User.model_validate(tweet.author).model_dump()
    author_dict['followers_count'] = len(tweet.author.followers)
    author_dict['following_count'] = len(tweet.author.following)
    author_dict['tweets_count'] = len(tweet.author.tweets)
    tweet_dict['author'] = author_dict
    
    return tweet_dict


@router.post("/", response_model=schemas.TweetWithAuthor, status_code=status.HTTP_201_CREATED)
def create_tweet(
    tweet: schemas.TweetCreate,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new tweet"""
    # Validate reply_to_id if provided
    if tweet.reply_to_id:
        reply_tweet = db.query(models.Tweet).filter(
            models.Tweet.id == tweet.reply_to_id
        ).first()
        if not reply_tweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tweet to reply to not found"
            )
    
    # Validate retweet_of_id if provided
    if tweet.retweet_of_id:
        retweet_tweet = db.query(models.Tweet).filter(
            models.Tweet.id == tweet.retweet_of_id
        ).first()
        if not retweet_tweet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tweet to retweet not found"
            )
    
    db_tweet = models.Tweet(
        content=tweet.content,
        author_id=current_user.id,
        reply_to_id=tweet.reply_to_id,
        retweet_of_id=tweet.retweet_of_id
    )
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    
    return _tweet_to_dict(db_tweet, current_user)


@router.get("/", response_model=List[schemas.TweetWithAuthor])
def list_tweets(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """List all tweets (public feed)"""
    tweets = db.query(models.Tweet).order_by(
        desc(models.Tweet.created_at)
    ).offset(skip).limit(limit).all()
    
    return [_tweet_to_dict(tweet, current_user) for tweet in tweets]


@router.get("/timeline", response_model=schemas.TimelineResponse)
def get_timeline(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get personalized timeline (tweets from followed users + own tweets)"""
    # Get IDs of users being followed
    following_ids = [user.id for user in current_user.following]
    following_ids.append(current_user.id)  # Include own tweets
    
    # Query tweets from followed users
    skip = (page - 1) * page_size
    tweets_query = db.query(models.Tweet).filter(
        models.Tweet.author_id.in_(following_ids)
    ).order_by(desc(models.Tweet.created_at))
    
    total = tweets_query.count()
    tweets = tweets_query.offset(skip).limit(page_size).all()
    
    return {
        "tweets": [_tweet_to_dict(tweet, current_user) for tweet in tweets],
        "total": total,
        "page": page,
        "page_size": page_size
    }


@router.get("/{tweet_id}", response_model=schemas.TweetWithAuthor)
def get_tweet(
    tweet_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """Get a specific tweet by ID"""
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found"
        )
    
    return _tweet_to_dict(tweet, current_user)


@router.put("/{tweet_id}", response_model=schemas.TweetWithAuthor)
def update_tweet(
    tweet_id: int,
    tweet_update: schemas.TweetUpdate,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update a tweet (only by the author)"""
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found"
        )
    
    if tweet.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this tweet"
        )
    
    tweet.content = tweet_update.content
    db.commit()
    db.refresh(tweet)
    
    return _tweet_to_dict(tweet, current_user)


@router.delete("/{tweet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tweet(
    tweet_id: int,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete a tweet (only by the author)"""
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found"
        )
    
    if tweet.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this tweet"
        )
    
    db.delete(tweet)
    db.commit()
    return None


@router.post("/{tweet_id}/like", response_model=schemas.LikeResponse)
def like_tweet(
    tweet_id: int,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Like a tweet"""
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found"
        )
    
    if current_user in tweet.liked_by:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already liked this tweet"
        )
    
    tweet.liked_by.append(current_user)
    db.commit()
    
    return {
        "message": "Tweet liked successfully",
        "is_liked": True,
        "likes_count": len(tweet.liked_by)
    }


@router.delete("/{tweet_id}/like", response_model=schemas.LikeResponse)
def unlike_tweet(
    tweet_id: int,
    current_user: models.User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Unlike a tweet"""
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found"
        )
    
    if current_user not in tweet.liked_by:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Haven't liked this tweet"
        )
    
    tweet.liked_by.remove(current_user)
    db.commit()
    
    return {
        "message": "Tweet unliked successfully",
        "is_liked": False,
        "likes_count": len(tweet.liked_by)
    }


@router.get("/{tweet_id}/replies", response_model=List[schemas.TweetWithAuthor])
def get_tweet_replies(
    tweet_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """Get all replies to a specific tweet"""
    tweet = db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tweet not found"
        )
    
    replies = db.query(models.Tweet).filter(
        models.Tweet.reply_to_id == tweet_id
    ).order_by(desc(models.Tweet.created_at)).offset(skip).limit(limit).all()
    
    return [_tweet_to_dict(reply, current_user) for reply in replies]


@router.get("/user/{username}", response_model=List[schemas.TweetWithAuthor])
def get_user_tweets(
    username: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """Get all tweets by a specific user"""
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    tweets = db.query(models.Tweet).filter(
        models.Tweet.author_id == user.id
    ).order_by(desc(models.Tweet.created_at)).offset(skip).limit(limit).all()
    
    return [_tweet_to_dict(tweet, current_user) for tweet in tweets]
