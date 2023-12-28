from flask import render_template, flash, redirect
from flask_login import login_required, current_user

from runtime import app
from models import db
from models.posts import Posts

# Delete posts
@app.route('/post/delete/<int:id>')
@login_required
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)
    if post_to_delete.poster.id != current_user.id:
        return redirect("/404")
    flash(u"Deleting this Post can not be undone!", "warning")
    return render_template("delete_post.html",
                           post_to_delete = post_to_delete)    

@app.route('/post/delete_confirmed/<int:id>')
@login_required
def delete_post_confirmed(id):
    post_to_delete = Posts.query.get_or_404(id)
    if post_to_delete.poster.id != current_user.id:
        return redirect("/404")
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        #return a message
        flash(u"Blog Post was deleted successfully!","success")
        # Grab all the posts from the DB
        posts = Posts.query.order_by(Posts.date_posted)
        return render_template("posts.html",
                           posts = posts)
    except:
        # return an error message
        flash(u"Whoops! There was a problem deleting the Post! Try again!","danger")

    # Grab all the posts from the DB
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("posts.html",
                           posts = posts)    
