from db import db, Course, Assignment, User


# CLUBS --------------------------------------------------------------
def get_all_clubs():
    return [c.serialize() for c in Club.query.all()]

def create_club():
    new_club = Club(
        name=name,
        description=description
    )
    db.session.add(new_club)
    db.session.commit()
    return new_course.serialize()

def get_club_by_id(club_id):
    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return none
    return club.serialize()

def delete_club_by_id(club_id):
    club = Club.query.filter_by(id=club_id).first()
    if club is None:
        return None
    db.session.delete(club)
    db.session.commit()
    return club.serialize()

# EVENTS --------------------------------------------------------------
def create_event():
    new event = Event(
        name=name,
        description=description,
        date=date,
        budget=budget,
        active=True
    )
    db.session.add(new_club)
    db.session.commit()
    return new_task.serialize()

def get_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    return event.serialize()

def finish_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    event.active = False
    db.session.commit()
    return event.serialize()

def delete_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    db.session.delete(event)
    db.session.commit()
    return club.serialize()

# TASKS --------------------------------------------------------------
def create_task():
    new_task = Task(
        name=name,
        description=description,
        date=date,
        budget=budget,
        active=True
    )
    db.session.add(new_club)
    db.session.commit()
    return new_task.serialize()

def get_task_by_id(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        return None
    return task.serialize()

def finish_event_by_id(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.active = False
    db.session.commit()
    return task.serialize()

# USERS ---------------------------------------------------------------
def create_user(name, netid):
    new_user = User(
        name=name,
        email=email,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

# TODO: assign user to club, assign user to event, assign user to task
