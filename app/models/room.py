from ..utils.dbo import db
from sqlalchemy.sql import func

class Room(db.Model):
    __tablename__ = "troom"
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=func.now())

    def __init__(self, room_name):
        self.room_name = room_name

    def json(self):
        return {
            "room_id": self.room_id,
            "room_name": self.room_name
        }

