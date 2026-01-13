from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    bio: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    bio: Optional[str] = None
    password: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    followers_count: int = 0
    following_count: int = 0
    tweets_count: int = 0

    class Config:
        from_attributes = True


class UserProfile(User):
    pass


# Tweet Schemas
class TweetBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=280)


class TweetCreate(TweetBase):
    reply_to_id: Optional[int] = None
    retweet_of_id: Optional[int] = None


class TweetUpdate(BaseModel):
    content: str = Field(..., min_length=1, max_length=280)


class Tweet(TweetBase):
    id: int
    created_at: datetime
    updated_at: datetime
    author_id: int
    reply_to_id: Optional[int] = None
    retweet_of_id: Optional[int] = None
    likes_count: int = 0
    replies_count: int = 0
    retweets_count: int = 0
    is_liked: bool = False

    class Config:
        from_attributes = True


class TweetWithAuthor(Tweet):
    author: User


# Auth Schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Login(BaseModel):
    username: str
    password: str


# WebSocket Schemas
class WSMessage(BaseModel):
    type: str  # "new_tweet", "new_like", "new_follow", "notification"
    data: dict
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Response Schemas
class FollowResponse(BaseModel):
    message: str
    is_following: bool


class LikeResponse(BaseModel):
    message: str
    is_liked: bool
    likes_count: int


class TimelineResponse(BaseModel):
    tweets: List[TweetWithAuthor]
    total: int
    page: int
    page_size: int
