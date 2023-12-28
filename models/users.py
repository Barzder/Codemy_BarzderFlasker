
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from models import db

# Create Users Model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    favorite_color = db.Column(db.String(120))
    about_author = db.Column(db.Text(500), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    profile_pic = db.Column(db.String(500), nullable=True, default="default_profile_pic.png")
    # Do some Password stuff
    password_hash = db.Column(db.String(128))
    # Users can have many posts
    posts = db.relationship('Posts', backref='poster')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name
