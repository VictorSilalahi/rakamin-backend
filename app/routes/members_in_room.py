from flask_restful import Resource
from flask import request
from sqlalchemy import text
from ..utils.dbo import db
from flask_jwt_extended import jwt_required


class MembersInRoom(Resource):
    @jwt_required()
    def get(self):
        room_id = request.args.get("room_id")
        members_in_room = db.session.execute(
            text(
                "select tmember.member_id, tmember.username, tmember.email, exists(select * from troommember where troommember.member_id=tmember.member_id and troommember.room_id="
                + room_id
                + ") as in_room from tmember where tmember.member_type='Reguler'"
            )
        )

        mr = [list(m) for m in members_in_room]

        return {"msg": "ok", "data": mr}, 200

    @jwt_required()
    def post(self):
        pass

    def put(self):
        pass

    @jwt_required()
    def delete(self):
        pass
