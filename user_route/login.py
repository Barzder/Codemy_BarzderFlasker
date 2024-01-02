from flask import render_template, flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash

from app import app
from webforms.login_form import LoginForm
from models.users import Users

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        # If the user exists than Check the hash
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash(u"Login successfull!","success")
            return redirect(url_for('dashboard'))
        else:
            flash(u"Login credentials incorrect! Try again!","danger")
    return render_template('login.html', 
                           form=form)
