from db import db, Course, Assignment, User


""" Club: get all, create, delete """
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


""" Events: get all, create, assign user """
def create_event():
    new event = Event(
        name=name,
        description=description,
        date=date,
        budget=budget,
        active=active
    )

""" Task: get all, create, assign user """
