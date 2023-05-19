from flask_restful import Resource
from flask import request
from ..models.member import Member
from ..utils.dbo import db
from flask_jwt_extended import jwt_required

class MembersAdminRoute(Resource):

    @jwt_required()
    def get(self):
        members = db.session.query(Member).filter(Member.member_type=="Reguler").all()
        return {"msg": "ok", 'data': list(x.json() for x in members)}, 200

    
    def post(self):
        pass

    def put(self):
        pass

    
    @jwt_required()
    def delete(self):
        member_id = request.form['member_id']
        member_to_delete = db.session.query(Member).filter_by(member_id=member_id).first()

        db.session.delete(member_to_delete)
        db.session.commit()
        
        return {"msg":"ok", "data":"member with id={0} has been deleted!".format(member_id) }, 200

