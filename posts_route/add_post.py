from flask import redirect, flash, render_template, flash, url_for
from flask_login import current_user

from app import app
from models import db
from webforms.post_form import PostForm
from models.posts import Posts

# Add Post Page
@app.route('/add-post', methods=['GET', 'POST'])
# @login_required
def add_post():
    form=PostForm()

    if form.validate_on_submit():
        poster = current_user.id
        post = Posts(
            title = form.title.data,
            content = form.content.data,
            # author = form.author.data,
            poster_id = poster,
            slug = form.slug.data)
        # Clear the form
        form.title.data = ''
        form.content.data = ''
        form.slug.data = ''

        # Add data to the database
        db.session.add(post)
        db.session.commit()

        # return a message
        flash(u"Post submitted successfully!","success")
        return redirect(url_for('post',
                                id=post.id,
                                slug=post.slug))

    # return to the webpage
    return render_template("add_post.html", form=form)
