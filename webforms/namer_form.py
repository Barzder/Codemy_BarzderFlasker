from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Whats your Name Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
    # Fieldtypes:
        # BooleanField
        # DateField
        # DateTimeField
        # DecimalField
        # FileField
        # HiddenField
        # MultipleField
        # FieldList
        # FloatField
        # FormField
        # IntegerField
        # PasswordField
        # RadioField
        # SelectField
        # SelectMultipleField
        # SubmitField
        # StingField
        # TextAreaField
    # Validators
        # DataRequired
        # Email
        # EqualTo
        # InputRequired
        # IPAddress
        # Length
        # MacAddress
        # NumberRange
        # Optional
        # Regexp
        # URL
        # UUID
        # AnyOf
        # NoneOf
