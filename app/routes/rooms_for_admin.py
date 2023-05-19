from flask_restful import Resource
from flask import request
from sqlalchemy import text
from ..models.room import Room
from ..utils.dbo import db
from flask_jwt_extended import jwt_required

class RoomsAdminRoute(Resource):

    @jwt_required()
    def get(self):
        rooms_and_members = db.session.execute(text("select troom.room_id, troom.room_name, count(troommember.*) as member_count from troom left join troommember ON troom.room_id = troommember.room_id group by troom.room_id"))

        rm = [list(r) for r in rooms_and_members]

        return {"msg": "ok", 'data': rm}, 200

    @jwt_required()
    def post(self):
        room_name = request.form['room_name']

        new_room = Room(room_name=room_name)
        db.session.add(new_room)
        db.session.commit()
        
        return {"msg":"ok", "data":"new room has been created!"}, 200
        

    def put(self):
        pass

    
    @jwt_required()
    def delete(self):
        room_id = request.form['room_id']

        room_to_delete = db.session.query(Room).filter_by(room_id=room_id).first()
        db.session.delete(room_to_delete)
        db.session.commit()
        
        return {"msg":"ok", "data":"room with id={0} has been deleted!".format(room_id) }, 200

