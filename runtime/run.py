from runtime import app, login_manager
from models.users import Users
from webforms.search_form import SearchForm

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Pass Stuff to the navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(searchform=form)
