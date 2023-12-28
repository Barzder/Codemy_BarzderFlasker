from flask import render_template
from flask_login import login_required

from runtime import app
from models.posts import Posts

# individual Post pages
@app.route('/posts/<int:id>_<string:slug>')
def post(id,slug):
    post = Posts.query.get_or_404(id)

    return render_template("post.html",
                           post = post)
