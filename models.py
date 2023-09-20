from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

# User model represents a user in the system.
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  # Unique identifier for the user as a text-based UUID.
    name = db.Column(db.String(255))  # The user's name.
    email = db.Column(db.String(255))  # The user's email address.
    avatar = db.Column(db.String(255))  # URL to the user's avatar.

# Group model represents a group or community in the system.
class Group(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  # Unique identifier for the group as a text-based UUID.
    title = db.Column(db.String(255))  # The title or name of the group.

# UserGroup model represents the relationship between users and groups.
class UserGroup(db.Model):
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), primary_key=True)  # Foreign key to the User model as a text-based UUID.
    group_id = db.Column(db.String(36), db.ForeignKey('group.id'), primary_key=True)  # Foreign key to the Group model as a text-based UUID.

# Event model represents an event in the system.
class Event(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  # Unique identifier for the event as a text-based UUID.
    title = db.Column(db.String(255))  # The title or name of the event.
    description = db.Column(db.String(255))  # A description of the event.
    creator = db.Column(db.String(36), db.ForeignKey('user.id'))  # Foreign key to the User model representing the event's creator.
    location = db.Column(db.String(255))  # The location of the event.
    start_date = db.Column(db.Date)  # The date when the event starts.
    end_date = db.Column(db.Date)  # The date when the event ends.
    start_time = db.Column(db.TIMESTAMP)  # The timestamp when the event starts.
    end_time = db.Column(db.TIMESTAMP)  # The timestamp when the event ends.
    thumbnail = db.Column(db.String(255))  # URL to the event's thumbnail image.

# GroupEvent model represents the relationship between groups and events.
class GroupEvent(db.Model):
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), primary_key=True)  # Foreign key to the Event model.
    group_id = db.Column(db.String(36), db.ForeignKey('group.id'), primary_key=True)  # Foreign key to the Group model.

# InterestedEvent model represents the relationship between users and events they are interested in.
class InterestedEvent(db.Model):
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), primary_key=True)  # Foreign key to the User model.
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'), primary_key=True)  # Foreign key to the Event model.

# Comment model represents a comment on an event.
class Comment(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  # Unique identifier for the comment as a text-based UUID.
    body = db.Column(db.String(255))  # Text content of the comment.
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))  # Foreign key to the User model representing the comment's author.
    event_id = db.Column(db.String(36), db.ForeignKey('event.id'))  # Foreign key to the Event model representing the event the comment is on.

# Image model represents an image associated with a comment.
class Image(db.Model):
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)  # Unique identifier for the image as a text-based UUID.
    comment_id = db.Column(db.String(36), db.ForeignKey('comment.id'))  # Foreign key to the Comment model representing the comment the image is associated with.
    image_url = db.Column(db.String(255))  # URL to the image.

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
