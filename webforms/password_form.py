from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# Create a Password validation Form
class PasswordForm(FlaskForm):
#    email = StringField("What's your email?", validators=[DataRequired()])
    password_hash = PasswordField("What's your passsword?", validators=[DataRequired()])
    submit = SubmitField("Submit")
