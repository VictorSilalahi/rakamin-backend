from flask_socketio import emit, join_room, leave_room, send

from run import sio
# from run import app

@sio.on("connect")
def new_connection(data):
    print("new connection has established!")

@sio.on('join_room')
def join_room_event(data):
    join_room(data["room_id"])


@sio.on('text')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    # room = session.get('room')
    # emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@sio.on('left')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    # room = session.get('room')
    # leave_room(room)
    # emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

@sio.on("disconnect")
def disconnect():
    print("client has disconnected!")