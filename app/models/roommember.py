from ..utils.dbo import db
from datetime import datetime


class RoomMember(db.Model):
    __tablename__ = "troommember"
    roommember_id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("troom.room_id"))
    member_id = db.Column(db.Integer, db.ForeignKey("tmember.member_id"))

    def __init__(self, room_id, member_id):
        self.room_id = room_id
        self.member_id = member_id

    def json(self):
        return {
            "room_id": self.room_id,
            "member_id": self.member_id
        }


