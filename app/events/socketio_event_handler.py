from flask_socketio import emit, join_room, leave_room

from run import s
from run import app

@socketio.on('join_room')
def join_room_event(data):
    app.logger.info("{0} has joined the room {1}".format(data["username"], data["room_id"]))
    join_room(data["room_id"])


@socketio.on('text')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    # room = session.get('room')
    # emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    # room = session.get('room')
    # leave_room(room)
    # emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)