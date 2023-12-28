from flask import flash, render_template
from werkzeug.security import generate_password_hash

from runtime import app
from models import db
from webforms.user_form import UserForm
from models.users import Users

# Create Add User Page
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash the password
            hashed_pw = generate_password_hash(form.password_hash.data, method='pbkdf2:sha3_256')
            user = Users(name=form.name.data, 
                         username=form.username.data, 
                         email=form.email.data, 
                         favorite_color=form.favorite_color.data,
                         about_author=form.about_author.data,
                         password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.username.data = ''
        form.email.data = ''
        form.favorite_color.data = ''
        form.about_author.data = ''
        form.password_hash.data = ''
        flash(u'User Added Successfully!','success')
    return render_template("add_user.html", 
        form=form,
        name=name,
        )
