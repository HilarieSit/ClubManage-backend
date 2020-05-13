from flask import Flask, request
from db import db
import dao
import json

app = Flask(__name__)
db_filename = "club.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


### ROUTES

# USERS
@app.route('/')
def hello():
    return "ClubManage: Club Management Application", 200

@app.route('/api/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        name = body.get('name'),
        email = body.get('email'),
        password = body.get('password')
    )
    return success_response(user, 201)

@app.route('/api/users/<int:user_id>/')
def get_user(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found")
    return success_response(user)

@app.route('/api/clubs/<int:cid>/<int:uid>/', methods=['POST'])
def delete_club_from_user(cid=None, uid=None):
    body = json.loads(request.data)
    user_type = body.get("type")
    user = dao.delete_club_from_user(cid, uid, user_type)
    if user is None:
        return failure_response("User not found")
    return success_response(user)


# CLUBS
@app.route('/api/clubs/')
def get_clubs():
    return success_response(dao.get_all_clubs())

@app.route('/api/clubs/', methods=['POST'])
def create_club():
    body = json.loads(request.data)
    club = dao.create_club(
        name = body.get('name'),
        description = body.get('description')
    )
    return success_response(club, 201)

@app.route('/api/clubs/<int:club_id>/', methods=['DELETE'])
def delete_club(club_id):
    club = dao.delete_club_by_id(club_id)
    if club is None:
        return failure_response("Club not found")
    return success_response(club)

@app.route('/api/clubs/<int:club_id>/', methods=['GET'])
def get_club(club_id):
    club = dao.get_club_by_id(club_id)
    if club is None:
        return failure_response("Club not found")
    return success_response(club)

@app.route('/api/clubs/<int:club_id>/', methods=['POST'])
def update_club(club_id):
    body = json.loads(request.data)
    club = dao.update_club_by_id(club_id, body)
    if club is None:
        return failure_response("Club not found")
    return success_response(club)

@app.route('/api/clubs/<int:club_id>/requests/', methods=['GET'])
def get_join_requests(club_id):
    join_requests = dao.get_join_requests(club_id)
    if join_requests is None:
        return failure_response("Club not found")
    return success_response(join_requests)


# EVENTS
@app.route('/api/clubs/<int:club_id>/events/', methods=['POST'])
def create_event(club_id):
    body = json.loads(request.data)
    new_event = dao.create_event(
        name = body.get('name'),
        date = body.get('date'),
        description = body.get('description'),
        budget = body.get('budget'),
        location = body.get('location'),
        time = body.get('time'),
    )
    event = dao.addclub2event(new_event.get('id'), club_id)
    return success_response(event, 201)

@app.route('/api/events/<int:event_id>/', methods=['DELETE'])
def delete_event(event_id):
    event = dao.delete_event_by_id(event_id)
    if event is None:
        return failure_response("Event not found")
    return success_response(event)

@app.route('/api/events/<int:event_id>/addclub/', methods=['POST'])
def add_club_to_event(event_id):
    body = json.loads(request.data)
    club_id = body.get('club_id')
    club = dao.get_club_by_id(club_id)
    if club is None:
        return failure_response("Club not found")
    event = dao.addclub2event(
        event_id = event_id,
        club_id = club_id
    )
    return success_response(event)

@app.route('/api/events/<int:event_id>/', methods=['GET'])
def get_event(event_id):
    event = dao.get_event_by_id(event_id)
    if event is None:
        return failure_response("Event not found")
    return success_response(event)

@app.route('/api/events/<int:event_id>/', methods=['POST'])
def update_event(event_id):
    body = json.loads(request.data)
    event = dao.update_event_by_id(event_id, body)
    if event is None:
        return failure_response("Event not found")
    return success_response(event)
    

# TASKS
@app.route('/api/events/<int:event_id>/tasks/', methods=['POST'])
def create_task(event_id):
    event = dao.get_event_by_id(event_id)
    if event is None:
        return failure_response("Event not found - need to create task with event")
    body = json.loads(request.data)
    task = dao.create_task(
        name = body.get('name'),
        description = body.get('description'),
        date = body.get('date'),
        budget = body.get('budget'),
        event_id = event_id
    )
    return success_response(task)

@app.route('/api/tasks/<int:task_id>/', methods=['DELETE'])
def delete_task(task_id):
    task = dao.delete_task_by_id(task_id)
    if task is None:
        return failure_response("Task not found")
    return success_response(task)

@app.route('/api/tasks/<int:task_id>/')
def get_task(task_id):
    task = dao.get_task_by_id(task_id)
    if task is None:
        return failure_response("Task not found")
    return success_response(task)


# REQUEST
@app.route('/api/addrequest/', methods=['POST'])
def addrequest():
    body = json.loads(request.data)
    # request to join club requires admin approval
    addrequest = dao.create_request(
        user_id = body.get("user_id"),
        club_id = body.get("club_id"),
        message = body.get("message"),
        accepted = body.get("accepted")
    )
    return success_response(addrequest, 201)

@app.route('/api/clubs/<int:club_id>/adduser/', methods=['POST'])
def add_user_to_club(club_id):
    body = json.loads(request.data)
    club = dao.adduser2club(body.get('user_id'), club_id, body.get('type'))
    if club is None:
        return failure_response("Club not found")
    return success_response(club)

@app.route('/api/events/<int:event_id>/adduser/', methods=['POST'])
def add_user_to_event(event_id):
    body = json.loads(request.data)
    event = dao.addevent2user(body.get('user_id'), event_id)
    if event is None:
        return failure_response("Event not found")
    return success_response(event)

@app.route('/api/tasks/<int:task_id>/adduser/', methods=['POST'])
def add_user_to_task(task_id):
    body = json.loads(request.data)
    task = dao.addtask2user(body.get('user_id'), task_id)
    if task is None:
        return failure_response("Task not found")
    return success_response(task)

@app.route('/api/addrequest/<int:request_id>/', methods=['POST'])
def accept_deny_request(request_id):
    body = json.loads(request.data)
    addreq = dao.get_request_by_id(request_id)
    if addreq is None:
        return failure_response("Request not found")
    current_state = addreq.get('accepted')
    if current_state is None:
        user_id = addreq.get("user_id")
        club_id = addreq.get("club_id")
        admin_response = body.get("accepted")
        if admin_response is True:
            # if accept member
            type = body.get('type')
            user = dao.adduser2club(user_id, club_id, type)
            return success_response(user)
        else:
            # if deny member
            user = dao.get_user_by_id(user_id)
            return success_response(user)
    # if accepted is not null, that means request is true or false
    return failure_response("Cannot change request already accepted/denied")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
