from flask import render_template

from runtime import app
from webforms.search_form import SearchForm
from models.posts import Posts

# Create Search Function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    posts = Posts.query
    post_searched = form.searched.data
    if form.validate_on_submit():
        posts = posts.filter(Posts.content.like('%' + post_searched + '%'))
        posts = posts.order_by(Posts.title).all()

    return render_template("search.html", 
        form = form,
        searched = post_searched,
        posts = posts
        )
