from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_migrate import Migrate

from waitress import serve

from dotenv import load_dotenv
import os

from app.utils import dbo
from app.utils.socketio import sio

from app.routes.admin import AdminRoute
from app.routes.members_for_admin import MembersAdminRoute
from app.routes.rooms_for_admin import RoomsAdminRoute
from app.routes.members_in_room import MembersInRoom
from app.routes.set_member_in_room import SetMemberInRoom

from app.routes.members import MembersRoute
from app.routes.member_validate import MemberValidateRoute
from app.routes.my_rooms import MyRoom


m = Migrate()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config["JWT_SECRET_KEY"] = os.getenv("RAKAMIN_JWT_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://" + os.getenv("RAKAMIN_DB_USERNAME")+":"+os.getenv("RAKAMIN_DB_PASSWORD")+"@"+os.getenv("RAKAMIN_DB_HOST")+":"+os.getenv("RAKAMIN_DB_PORT")+"/"+os.getenv("RAKAMIN_DB_NAME")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config['UPLOAD_FOLDER'] = os.getenv("APP_UPLOAD_FOLDER")

    # from app.models.member import Member
    # from app.models.room import Room
    # from app.models.roommember import RoomMember
    # from app.models.conversation import Conversation

    dbo.init_app(app)
    m.init_app(app, dbo.db)

    jwt = JWTManager(app)

    api = Api(app)

    api.add_resource(AdminRoute, "/api/admin/validate")
    api.add_resource(MembersAdminRoute, "/api/admin/members")
    api.add_resource(RoomsAdminRoute, "/api/admin/rooms")
    api.add_resource(MembersInRoom, "/api/admin/room/members")
    api.add_resource(SetMemberInRoom, "/api/admin/room/setmember")

    api.add_resource(MembersRoute, "/api/members")
    api.add_resource(MemberValidateRoute, "/api/member/validate")
    api.add_resource(MyRoom, "/api/member/rooms")


    CORS(app)

    sio.init_app(app, cors_allowed_origins="*")
    from app.events import socketio_event_handler

    return app, sio


if __name__ == "__main__":
    app, sio = create_app()
    if os.getenv("RAKAMIN_MODE") == "dev":
        # app.run(
        #     host=os.getenv("RAKAMIN_HOST"), port=os.getenv("RAKAMIN_PORT"), debug=True
        # )
        sio.run(
            app, host=os.getenv("RAKAMIN_HOST"), port=os.getenv("RAKAMIN_PORT"), debug=True
        )
    else:
        # serve(
        #     app, host=os.getenv("RAKAMIN_HOST"), port=os.getenv("RAKAMIN_PORT")
        # )
        sio.run(
            app, host=os.getenv("RAKAMIN_HOST"), port=os.getenv("RAKAMIN_PORT")
        )
