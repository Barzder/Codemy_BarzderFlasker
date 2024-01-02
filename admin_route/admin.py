from flask import redirect, render_template
from flask_login import login_required, current_user

from app import app
from models.users import Users

# Admin Page
@app.route('/admin')
@login_required
def admin():
    if current_user.is_admin == False:
        return redirect("/404")
    our_users = Users.query.order_by(Users.date_added) 
    return render_template("admin.html",
        our_users=our_users)
