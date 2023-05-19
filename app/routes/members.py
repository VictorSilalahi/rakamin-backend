from flask_restful import Resource
from flask import request
from ..models.member import Member
from ..utils.dbo import db
from werkzeug.security import generate_password_hash


class MembersRoute(Resource):
    
    def get(self):
        members = db.session.query(Member).all()

        return {"msg":"ok", 'data':list(x.json() for x in members)}, 200

    def post(self):
        email = request.form['email']

        member = db.session.query(Member).filter_by(email=email).first()
        if member:
            return {"msg": "error", "data": "this email has been registered!"}, 400

        username = request.form['username']
        member_pwd = generate_password_hash(request.form['password'])
        print(member_pwd)
        new_member = Member(username=username, email=email, password=member_pwd)
        db.session.add(new_member)
        db.session.commit()
        
        return {"msg":"ok", "data":"new member has been created!" }, 201

    def put(self):
        pass

    def delete(self):
        pass
