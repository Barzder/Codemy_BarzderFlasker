from flask import Flask
from flask_ckeditor import CKEditor
from flask_login import LoginManager

# Create a Flask Instance
app = Flask(__name__)

# add CKeditor to the app:
ckeditor = CKEditor(app)

# Flask Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'