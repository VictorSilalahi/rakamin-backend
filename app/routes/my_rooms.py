from flask_restful import Resource
from flask import request
from ..models.roommember import RoomMember
from sqlalchemy import text
from ..utils.dbo import db
from flask_jwt_extended import jwt_required

class MyRoom(Resource):

    @jwt_required()
    def get(self):
        member_id = request.args.get("member_id")

        my_rooms = db.session.execute(text("select distinct troom.room_id, troom.room_name from troom, troommember where troom.room_id=troommember.room_id and troommember.member_id="+member_id))
        myr = [list(mr) for mr in my_rooms]
        
        return {"msg":"ok", "data": myr}, 200
        

    @jwt_required()
    def post(self):
        pass        

    def put(self):
        pass

    
    def delete(self):
        pass
