from flask import Flask, render_template
from models import db, User, Group, UserGroup, Event, GroupEvent, InterestedEvent, Comment, Image, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_app.db'

# Initialize the database
init_db(app)

# Routes
@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/event/<event_id>')
def event_details(event_id):
    event = Event.query.get(event_id)
    return render_template('event_details.html', event=event)

if __name__ == '__main__':
    app.run(debug=True)
