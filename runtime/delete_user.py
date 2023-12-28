from flask import redirect, flash, render_template, url_for
from flask_login import login_required, current_user

from runtime import app
from models import db
from webforms.user_form import UserForm
from models.users import Users

# Create Delete User Route
@app.route('/delete_user/<int:id>')
@login_required
def delete_user(id):
    if id != current_user.id and current_user.is_admin == False:
        return redirect("/404")
    user_to_delete = Users.query.get_or_404(id)
    if id == current_user.id:
        flash(u"You will not be able to log into this website anymore. Your account can not be restored.", "warning")
    else:
        flash(u"The user will not be able to log into this website anymore. The account can not be restored.", "warning")
    return render_template("delete_user.html", user_to_delete=user_to_delete)

@app.route('/delete_user_confirmed/<int:id>')
@login_required
def delete_user_confirmed(id):
    if id != current_user.id and current_user.is_admin == False:
        return redirect("/404")
    user_to_delete = Users.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash(u"User Deleted Successfully!","success")
        if current_user.is_admin == True:
            our_users = Users.query.order_by(Users.date_added)
            return render_template("admin.html",
                our_users=our_users)
        return redirect(url_for('login'))
    except:
        flash(u"There was a problem deleting the user!","danger")
        if current_user.is_admin == True:
            our_users = Users.query.order_by(Users.date_added)
            return render_template("admin.html",
                our_users=our_users)
        return redirect(url_for('dashboard'))