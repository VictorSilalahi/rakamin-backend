from ..utils.dbo import db
from datetime import datetime
from sqlalchemy.sql import func

class Conversation(db.Model):
    __tablename__ = "tconversation"
    conversation_id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("troom.room_id"))
    member_id = db.Column(db.Integer, db.ForeignKey("tmember.member_id"))
    message = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=func.now())

    def __init__(self, room_id, member_id, message):
        self.room_id = room_id
        self.member_id = member_id
        self.message = message

    def json(self):
        return {
            "room_id": self.room_id,
            "member_id": self.member_id
        }


