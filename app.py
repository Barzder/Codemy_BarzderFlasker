from runtime import app
import yaml

# Get the config infos from the YAML file:
with open('config.yml','r') as yamlConfigFile:
    yamlConfigData = yaml.safe_load(yamlConfigFile)
yamlConfigDatabaseConnection = yamlConfigData['configDatabaseConnection']
yamlConfigSecretKey = yamlConfigData['configSecretKey']

# Add database connection
app.config['SQLALCHEMY_DATABASE_URI'] = yamlConfigDatabaseConnection

# Secret key!
app.config['SECRET_KEY'] = yamlConfigSecretKey

import runtime
from models import db
from runtime import run

# Designate An Update Folder
UPLOAD_FOLDER = 'static/images/user_profile_pics'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from runtime import error, default_route, about_author, add_post, add_user, admin, dashboard, delete_post, delete_user, edit_post, get_current_date
from runtime import login, logout, name, post, posts, search, set_admin, test_pw, update, user

if "__name__" == "__main__":
    app.run(debug="true")