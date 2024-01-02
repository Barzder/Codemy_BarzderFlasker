from flask import request, redirect, flash, render_template
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

import uuid as uuid
import os

from app import app
from models import db
from webforms.user_form import UserForm
from models.users import Users

# Update User Page
@app.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    if id != current_user.id:
        return redirect("/404")
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.username = request.form['username']
        name_to_update.email = request.form['email']
        name_to_update.favorite_color = request.form['favorite_color']
        name_to_update.about_author = request.form['about_author']
        if request.files['profile_pic']:
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], name_to_update.profile_pic)) and name_to_update.profile_pic != "default_profile_pic.png":
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], name_to_update.profile_pic))
            profile_pic = request.files['profile_pic']
            # Grab Image Name Securely
            profile_pic_filename = secure_filename(profile_pic.filename)
            # Set UUID
            name_to_update.profile_pic = str(uuid.uuid1()) + "_" + profile_pic_filename
            # Save The Image
            profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], name_to_update.profile_pic))
        try:
            db.session.commit()
            flash(u"User Updated Succesfully","success")
            return redirect("/dashboard")
        except:
            flash(u"Error! Looks like there was a problem!","danger")
            return render_template("update.html",
                                   form = form,
                                   name_to_update = name_to_update,
                                   id = id)
    else:
        return render_template("update.html",
                                   form = form,
                                   name_to_update = name_to_update,
                                   id = id)
