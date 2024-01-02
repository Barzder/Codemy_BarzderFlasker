from flask import render_template
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash

from app import app
from webforms.password_form import PasswordForm
from models.users import Users

# Create Password Test Page
@app.route('/test_pw', methods=['GET', 'POST'])
@login_required
def test_pw():
    email = None
    password = None
    user_to_check = None
    passed = None
    form = PasswordForm()
    if form.validate_on_submit():
        password = form.password_hash.data
        form.password_hash = ''

        # Lookup User by Email address
        user_to_check = Users.query.get_or_404(current_user.id)

        # Check Hashed Password
        passed = check_password_hash(user_to_check.password_hash, password)

    return render_template('test_pw.html',
        email = email,
        password = password,
        user_to_check = user_to_check,
        passed = passed,
        form = form
        )
