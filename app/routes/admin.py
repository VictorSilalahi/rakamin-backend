from flask_restx import Resource
from flask import request
from ..models.member import Member
from ..utils.dbo import db
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

    

class AdminRoute(Resource):

    def get(self):
        pass

    def post(self):
        email = request.form['email']
        pwd = request.form['password']

        admin = db.session.query(Member).filter_by(email=email, member_type='admin').first()
        if not admin:
            return {"msg":"error", "data": "admin credential error!"}, 401


        if self.check_admin_password(admin.password, pwd):
            admin_data = {
                "member_id": admin.member_id,
                "pub_id": admin.pub_id,
                "username": admin.username,
                "email": admin.email
            }
            token_range = timedelta(days=7)
            token_refresh_range = timedelta(days=14)
            admin_token = create_access_token(identity=admin.member_id, fresh=True, expires_delta=token_range)
            admin_refresh_token = create_refresh_token(identity=admin.member_id, expires_delta=token_refresh_range)
            
            return {"msg":"ok", "token":admin_token, "refresh_token":admin_refresh_token, "data": admin_data}, 200

        else:
            return {"msg":"error", "data": "admin credential error!"}, 401

    def put(self):
        pass

    def delete(self):
        pass

    def check_admin_password(self, pwd1, pwd2):
        if pwd1 == pwd2:
            return True
        else:
            return False