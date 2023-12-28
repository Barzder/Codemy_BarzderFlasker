from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from runtime import app

# Initialize the Database   
db = SQLAlchemy(app)
migrate = Migrate(app, db)
