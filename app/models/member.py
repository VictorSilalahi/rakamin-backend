from ..utils.dbo import db
from uuid import uuid4
from sqlalchemy.sql import func


class Member(db.Model):
    __tablename__ = "tmember"
    member_id = db.Column(db.Integer, primary_key=True)
    pub_id = str(uuid4())
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    member_type = db.Column(db.String, default="Reguler")
    created_at = db.Column(db.DateTime, default=func.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def json(self):
        return {
            "member_id": self.member_id,
            "pub_id": self.pub_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.strftime("%m-%d-%Y"),
            "member_type": self.member_type,
        }
