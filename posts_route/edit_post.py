from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user

from app import app
from models import db
from webforms.post_form import PostForm
from models.posts import Posts

# Edit Post Page
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Posts.query.get_or_404(id)
    if post.poster.id != current_user.id:
        return redirect("/404")
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        # post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        # Update DB
        db.session.add(post)
        db.session.commit()
        flash(u"Post has been updated!","success")
        return redirect(url_for('post', id=post.id, slug=post.slug))
    form.title.data = post.title
    # form.author.data = post.author
    form.slug.data = post.slug
    form.content.data = post.content
    return render_template("update_post.html",
                           form = form,
                           post = post)
