from flask import redirect, render_template
from flask_login import current_user

from app import app
from models.posts import Posts

# Dashboard
@app.route('/about_author/<int:id>')
def about_author(id):
    post = Posts.query.get_or_404(id)
    if current_user.is_authenticated:
        if post.poster.id == current_user.id:
            return redirect ("/dashboard")
    return render_template('about_author.html',
                           post = post)
