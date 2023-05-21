from flask_socketio import emit, join_room, leave_room

from ..models.conversation import Conversation
from ..models.member import Member
from ..models.room import Room

from ..utils.dbo import db

from run import sio


@sio.on("connect")
def new_connection(data):
    print("new connection has established!")


@sio.on('join_room')
def join_room_event(data):
    rooms = data["room"]
    username = data["username"]
    member_id = data["member_id"]
    for r in rooms:
        join_room(r)
        print(username + " has joined in room:"+r)
        emit("join_room_announcement", {
            "member_id": member_id,
            "username": username,
            "room_name":r
        }, room=r)


@sio.on('send_message')
def handle_send_message_event(data):
    print("clint has sent a message to the room.")
    emit("receive_message", data, room=data["room_name"])

    room_name = data["room_name"]
    username = data["username"]
    message = data["message"]

    # save conversation to database
    room = db.session.query(Room).filter_by(room_name=room_name).first()
    member = db.session.query(Member).filter_by(username=username).first()

    new_conversation = Conversation(room_id=room.room_id, member_id=member.member_id, message=message)
    db.session.add(new_conversation)
    db.session.commit()


@sio.on('left_room')
def handle_left_room_event(data):
    print("a client has left the room "+data["room_name"])
    leave_room(data["room_name"])
    emit('has_left', {"room_name": data["room_name"], "message": data["username"] + " has left the room.", "username": data["username"]}, room=data["room_name"])


@sio.on("disconnect")
def disconnect():
    print("client has disconnected!")