from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# association tables
clubs_events_assoc = db.Table('clubs_events_assoc', db.Model.metadata,
    db.Column('club_id', db.Integer, db.ForeignKey('club.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

clubs_admins_assoc = db.Table('clubs_admins_assoc', db.Model.metadata,
    db.Column('club_id', db.Integer, db.ForeignKey('club.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

clubs_members_assoc = db.Table('clubs_members_assoc', db.Model.metadata,
    db.Column('club_id', db.Integer, db.ForeignKey('club.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

events_users_assoc = db.Table('events_user_assoc', db.Model.metadata,
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

tasks_users_assoc = db.Table('tasks_user_assoc', db.Model.metadata,
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin_clubs = db.relationship('Club', secondary=clubs_admins_assoc, back_populates='admins')
    member_clubs = db.relationship('Club', secondary=clubs_members_assoc, back_populates='members')
    events = db.relationship('Event', secondary=events_users_assoc, back_populates='users')
    tasks = db.relationship('Task', secondary=tasks_users_assoc, back_populates='users')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')

    def serialize(self, removed_item=None):
        all_clubs = [a.serialize_info() for a in self.admin_clubs]
        all_clubs.extend([m.serialize_info() for m in self.member_clubs])
        serialized_dict = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'clubs': all_clubs,
            'password': self.password,
            'events': [e.serialize_info() for e in self.events],
            'tasks': [t.serialize_info() for t in self.tasks],
        }
        if removed_item is not None:
            for item in removed_item:
                serialized_dict.pop(item)
        return serialized_dict

    def serialize_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class Club(db.Model):
    __tablename__ = 'club'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    events = db.relationship('Event', secondary=clubs_events_assoc, back_populates='clubs')
    admins = db.relationship('User', secondary=clubs_admins_assoc, back_populates='admin_clubs')
    members = db.relationship('User', secondary=clubs_members_assoc, back_populates='member_clubs')
    join_requests = db.relationship("JoinRequest", cascade="delete")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')

    def serialize(self, removed_item=None):
        serialized_dict = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'events': [e.serialize_info() for e in self.events],
            'admins': [a.serialize_info() for a in self.admins],
            'members': [m.serialize_info() for m in self.members]
        }
        if removed_item is not None:
            for item in removed_item:
                serialized_dict.pop(item)
        return serialized_dict

    def serialize_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def serialize_join_requests(self):
        return {
            'join_requests': [jr.serialize_info() for jr in self.join_requests]
        }



class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float, nullable=True)
    location = db.Column(db.String, nullable=True)
    time = db.Column(db.String, nullable=True)
    tasks = db.relationship('Task', cascade='delete')
    clubs = db.relationship('Club', secondary=clubs_events_assoc, back_populates='events')
    users = db.relationship('User', secondary=events_users_assoc, back_populates='events')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.date = kwargs.get('date', '')
        self.budget = kwargs.get('budget', '')

    def serialize(self, removed_item=None):
        serialized_dict = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'location': self.location,
            'time': self.time,
            'budget': self.budget,
            'tasks': [t.serialize_info() for t in self.tasks],
            'clubs': [c.serialize_info() for c in self.clubs],
            'users': [u.serialize_info() for u in self.users],
        }
        if removed_item is not None:
            for item in removed_item:
                serialized_dict.pop(item)
        return serialized_dict

    def serialize_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'location': self.location,
            'time': self.time,
            'budget': self.budget,
        }

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    users = db.relationship('User', secondary=tasks_users_assoc, back_populates='tasks')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.date = kwargs.get('date', '')
        self.budget = kwargs.get('budget', '')
        self.event_id = kwargs.get('event_id')

    def serialize(self, removed_item=None):
        serialized_dict = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'budget': self.budget,
            'users': [u.serialize_info() for u in self.users]
        }
        if removed_item is not None:
            for item in removed_item:
                serialized_dict.pop(item)
        return serialized_dict

    def serialize_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'budget': self.budget
        }

class JoinRequest(db.Model):
    __tablename__ = 'joinrequest'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    message = db.Column(db.String)
    accepted = db.Column(db.Boolean)

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', '')
        self.club_id = kwargs.get('club_id', '')
        self.message = kwargs.get('message', '')
        self.accepted = kwargs.get('accepted', '')

    def serialize(self, removed_item=None):
        serialized_dict = {
            'id': self.id,
            'user_id': self.user_id,
            'club_id': self.club_id,
            'message': self.message,
            'accepted': self.accepted
        }
        if removed_item is not None:
            for item in removed_item:
                serialized_dict.pop(item)
        return serialized_dict

    def serialize_info(self):
        serialized_dict = self.serialize()
        serialized_dict.pop('club_id', None)
        return serialized_dict