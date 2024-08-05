# backend/db/models/user_accounts.py
from mongoengine import Document, StringField, IntField, ListField, ReferenceField

class User(Document):
    user_id = IntField(primary_key=True)
    username = StringField(max_length=50, unique=True, required=True)
    email = StringField(max_length=100, unique=True, required=True)
    auth_method = StringField(max_length=50, required=True)
    password_hash = StringField(max_length=128, required=True)
    statistics = ListField(ReferenceField('Statistics'))

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"