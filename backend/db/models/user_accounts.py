# backend/db/models/user_accounts.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_accounts'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    auth_method = Column(String(50), nullable=False)
    password_hash = Column(String(128), nullable=False)
    statistics = relationship("Statistics", back_populates="user")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
