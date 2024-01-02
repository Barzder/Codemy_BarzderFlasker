from flask import redirect, render_template
from flask_login import login_required, current_user

from app import app
from models import db
from models.users import Users

# Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # Workaround for empty profile pic page:
    if current_user.profile_pic == None:
        user_to_update = Users.query.get_or_404(current_user.id)
        user_to_update.profile_pic = "default_profile_pic.png"
        try:
            db.session.commit()
        except:
            return redirect("/404")
    return render_template('dashboard.html')
