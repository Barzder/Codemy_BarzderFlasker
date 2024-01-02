from flask import redirect, url_for, flash
from flask_login import login_required, logout_user

from app import app

# Logout Page
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash(u"You have been logged out!","info")
    return redirect(url_for('login'))
