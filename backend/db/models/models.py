# backend/db/models/models.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from.user_accounts import User
from.extracted_stats import Statistics