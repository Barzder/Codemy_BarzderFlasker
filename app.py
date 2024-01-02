from flask import Flask
from flask_ckeditor import CKEditor
from flask_login import LoginManager

import yaml

# Get the config infos from the YAML file:
with open('config.yml','r') as yamlConfigFile:
    yamlConfigData = yaml.safe_load(yamlConfigFile)
yamlConfigDatabaseConnection = yamlConfigData['configDatabaseConnection']
yamlConfigSecretKey = yamlConfigData['configSecretKey']

# Create a Flask Instance
app = Flask(__name__)

# add CKeditor to the app:
ckeditor = CKEditor(app)

# Flask Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Add database connection
app.config['SQLALCHEMY_DATABASE_URI'] = yamlConfigDatabaseConnection

# Secret key!
app.config['SECRET_KEY'] = yamlConfigSecretKey

from models.users import Users
from webforms.search_form import SearchForm

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Pass Stuff to the navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(searchform=form)

# Designate An Update Folder
UPLOAD_FOLDER = 'static/images/user_profile_pics'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

"""
    Add all routes here!!!
"""
from admin_route import admin, set_admin
from default_route import default_route, errors
from misc_routes import get_current_date, name, user
from posts_route import add_post, delete_post, edit_post, post, posts, search
from user_route import about_author, add_user, dashboard, delete_user, login, logout, test_pw, update

if "__name__" == "__main__":
    app.run()