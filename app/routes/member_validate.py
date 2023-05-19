from flask_restful import Resource
from flask import request
from ..models.member import Member
from ..utils.dbo import db
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash
from datetime import timedelta

class MemberValidateRoute(Resource):
    
    def get(self):
        members = db.session.query(Member).all()

        return {"msg":"ok", 'data':list(x.json() for x in members)}, 200

    def post(self):
        email = request.form['email']
        pwd = request.form['password']

        member = db.session.query(Member).filter_by(email=email, member_type='Reguler').first()
        if not member:
            return {"msg":"error", "data": "admin credential error!"}, 401


        if check_password_hash(member.password, pwd):
            member_data = {
                "member_id": member.member_id,
                "pub_id": member.pub_id,
                "username": member.username,
                "email": member.email
            }
            token_range = timedelta(days=7)
            token_refresh_range = timedelta(days=14)
            member_token = create_access_token(identity=member.member_id, fresh=True, expires_delta=token_range)
            member_refresh_token = create_refresh_token(identity=member.member_id, expires_delta=token_refresh_range)
            
            return {"msg":"ok", "token":member_token, "refresh_token":member_refresh_token, "data": member_data}, 200

    def put(self):
        pass

    def delete(self):
        pass
