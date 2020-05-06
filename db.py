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

class Club(db.Model):
    """ many-to-many users
        many-to-many events """
    __tablename__ = 'club'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    events = db.relationship('Event', secondary=clubs_events_assoc, back_populates='clubs')
    admins = db.relationship('User', secondary=clubs_admins_assoc, back_populates='admin_clubs')
    members = db.relationship('User', secondary=clubs_members_assoc, back_populates='member_clubs')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.discription,
            'events': [e.serialize_no_course() for e in self.events],
            'admins': [a.serialize_no_course() for a in self.admins],
            'member's: [m.serialize_no_course() for m in self.members]
        }

class Events(db.Model):
    """ many-to-many clubs
        many-to-many users
        one-to-many tasks """
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    tasks = db.relationship('Task', cascade='delete')
    clubs = db.relationship('Club', secondary=clubs_events_assoc, back_populates='events')
    users = db.relationship('User', secondary=events_users_assoc, back_populates='events')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.budget = kwargs.get('budget', '')
        self.active = kwargs.get('active', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.discription,
            'budget': self.budget,
            'active': self.active,
            'events': [e.serialize_no_course() for e in self.events],
            'clubs': [c.serialize_no_course() for c in self.clubs],
            'users': [u.serialize_no_course() for u in self.users],
        }

class Task(db.Model):
    """ many-to-one events
        many-to-many users (member) """

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    events = db.relationship('Event', secondary=events_users_assoc, back_populates='users')
    admin_clubs = db.relationship('Club', secondary=clubs_admins_assoc, back_populates='admins')
    member_clubs = db.relationship('Club', secondary=clubs_members_assoc, back_populates='members')
    tasks = db.relationship('Tasks', back_populates='users')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'events': [e.serialize_no_course() for e in self.events],
            'clubs': [m.serialize_no_course() for m in self.member_clubs],
            'tasks': [t.serialize_no_course() for u in self.tasks],
        }


class Messages(db.Model):
