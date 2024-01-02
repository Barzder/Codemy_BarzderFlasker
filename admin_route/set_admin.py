from flask import redirect, flash, render_template
from flask_login import current_user

from app import app
from models import db
from models.users import Users

# Promote or Demote Admins
@app.route('/set_admin/<int:id>/<RS>')
def set_admin(id,RS):
    if current_user.is_admin == False:
        return redirect("/404")
    user_to_update = Users.query.get_or_404(id)
    if user_to_update.is_admin == True and RS == "reset":
        user_to_update.is_admin = False
    elif user_to_update.is_admin == False and RS == "set":
        user_to_update.is_admin = True
    elif user_to_update.is_admin == None:
        user_to_update.is_admin = False
    else:
        flash(u"Whoops, there was a problemd updating the priviliges of the user!","danger")
        our_users = Users.query.order_by(Users.date_added)
        return render_template("admin.html",
            our_users=our_users)
    try:
        db.session.commit()
        flash(u"User Priviliges Changed Successfully!","success")
    except:
        flash(u"Whoops, there was a problemd updating the priviliges of the user!","danger")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("admin.html",
        our_users=our_users)
