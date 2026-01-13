from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Association table for follows (many-to-many self-referential)
follows = Table(
    'follows',
    Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('followed_id', Integer, ForeignKey('users.id'), primary_key=True)
)

# Association table for tweet likes
likes = Table(
    'likes',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('tweet_id', Integer, ForeignKey('tweets.id'), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    bio = Column(Text)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    tweets = relationship("Tweet", back_populates="author", cascade="all, delete-orphan")
    
    # Self-referential many-to-many for follows
    following = relationship(
        "User",
        secondary=follows,
        primaryjoin=(follows.c.follower_id == id),
        secondaryjoin=(follows.c.followed_id == id),
        backref="followers"
    )
    
    # Many-to-many for liked tweets
    liked_tweets = relationship(
        "Tweet",
        secondary=likes,
        back_populates="liked_by"
    )


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    reply_to_id = Column(Integer, ForeignKey("tweets.id"), nullable=True)
    retweet_of_id = Column(Integer, ForeignKey("tweets.id"), nullable=True)
    
    # Relationships
    author = relationship("User", back_populates="tweets")
    liked_by = relationship(
        "User",
        secondary=likes,
        back_populates="liked_tweets"
    )
    
    # Self-referential for replies and retweets
    replies = relationship("Tweet", backref="reply_to", remote_side=[id], foreign_keys=[reply_to_id])
    retweets = relationship("Tweet", backref="retweet_of", remote_side=[id], foreign_keys=[retweet_of_id])
