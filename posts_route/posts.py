from flask import render_template

from app import app
from models.posts import Posts

# exsisting Posts
@app.route('/posts')
def posts():
    # Grab all the posts from the DB
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("posts.html",
                           posts = posts)
