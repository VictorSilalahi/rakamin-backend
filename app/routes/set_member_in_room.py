from flask_restful import Resource
from flask import request
from ..models.roommember import RoomMember
from sqlalchemy import text
from ..utils.dbo import db
from flask_jwt_extended import jwt_required

class SetMemberInRoom(Resource):

    def get(self):
        pass

    @jwt_required()
    def post(self):
        data = request.get_json()
        room_id = data['room_id']
        member_list = data['member_list']

        db.session.execute(text("delete from troommember where room_id="+room_id))
        db.session.commit()
        
        for ml in member_list:
            new_room_member = RoomMember(room_id=room_id, member_id=int(ml))
            db.session.add(new_room_member)
            db.session.commit()
        
        return {"msg":"ok", "data":"new room member has been set!"}, 200
        

    def put(self):
        pass

    
    def delete(self):
        pass
