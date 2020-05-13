from db import db, User, Club, Event, Task, JoinRequest

# USERS
def create_user(name, email, password):
    new_user = User(
        name=name,
        email=email,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize(removed_item=['password'])

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    # remove password
    return user.serialize(removed_item=['password'])


# CLUBS
def get_all_clubs():
    return [c.serialize(removed_item=['events', 'admins', 'members']) for c in Club.query.all()]

def create_club(name, description):
    new_club = Club(
        name=name,
        description=description
    )
    db.session.add(new_club)
    db.session.commit()
    return new_club.serialize()

def delete_club_by_id(club_id):
    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None
    db.session.delete(club)
    db.session.commit()
    return club.serialize()

def get_club_by_id(club_id):
    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None
    return club.serialize()

def update_club_by_id(club_id, body):
    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None
    club.name = body.get("name", club.name)
    club.description = body.get("description", club.description)
    db.session.commit()
    return club.serialize()

def get_join_requests(club_id):
    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None
    return club.serialize_join_requests()

# EVENTS
def create_event(name, description, date, budget, location, time):
    new_event = Event(
        name=name,
        description=description,
        date=date,
        budget=budget,
        location=location,
        time=time
    )
    db.session.add(new_event)
    db.session.commit()
    return new_event.serialize()

def addclub2event(event_id, club_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None

    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None

    event.clubs.append(club)
    db.session.commit()
    return event.serialize()

def delete_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    db.session.delete(event)
    db.session.commit()
    return event.serialize()

def get_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    return event.serialize()

def update_event_by_id(event_id,  body):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    event.name = body.get("name", event.name)
    event.date = body.get("date", event.date)
    event.description = body.get("description", event.description)
    event.budget = body.get("budget", event.budget)
    db.session.commit()
    return event.serialize()
    

# TASKS
def create_task(name, description, date, budget, event_id):
    new_task = Task(
        name=name,
        description=description,
        date=date,
        budget=budget,
        event_id=event_id
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task.serialize()

def delete_task_by_id(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        return None
    db.session.delete(task)
    db.session.commit()
    return task.serialize()

def get_task_by_id(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        return None
    return task.serialize()

# ADD REQUESTS
def create_request(user_id, club_id, message, accepted):
    new_request = JoinRequest(
        user_id=user_id,
        club_id=club_id,
        message=message,
        accepted=accepted
    )
    db.session.add(new_request)
    db.session.commit()
    return new_request.serialize()

def get_request_by_id(request_id):
    addrequest = JoinRequest.query.filter_by(id=request_id).first()
    if addrequest is None:
        return None
    return addrequest.serialize()

def adduser2club(user_id, club_id, type):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None

    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None

    if type == "admin":
        club.admins.append(user)
    else:
        club.members.append(user)
    db.session.commit()
    updated_club = Club.query.filter_by(id=club_id).first()
    return updated_club.serialize()

def addevent2user(user_id, event_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None

    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None

    user.events.append(event)
    db.session.commit()
    updated_event = Event.query.filter_by(id=event_id).first()
    return updated_event.serialize()

def delete_club_from_user(club_id, user_id, user_type):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None

    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None

    if(user_type == "member"):
        club.members.remove(user)
    if(user_type == "admin"):
        club.admins.remove(user)
    
    db.session.commit()
    updated_user= User.query.filter_by(id=user_id).first()
    return updated_user.serialize(removed_item=['password'])


def addtask2user(user_id, task_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None

    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        return None

    user.tasks.append(task)
    db.session.commit()
    updated_task = Task.query.filter_by(id=task_id).first()
    return updated_task.serialize()
