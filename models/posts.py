from datetime import datetime

from models import db

# Create a Blog Post Model
class Posts(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     title = db.Column(db.String(255))
     content = db.Column(db.Text)
     # author = db.Column(db.String(255))
     date_posted = db.Column(db.DateTime, default=datetime.utcnow)
     slug = db.Column(db.String(255))
     # Foreign key to link users (refer to primary key of Users)
     poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))
