from flask import render_template

from app import app

# Create a route decorator
@app.route('/')
    # Jinja2 Filters for variables:
        # safe (used for passing htmls, Jinja otherwise strips the html; or also passing other code that has to "executed")
        # capitalize (sets the first char to upper)
        # lower
        # upper
        # title
        # trim
        # striptags (removes tags that could be "executed")
def index():
    first_name = "John"
    stuff = "this is bold text"
    favorite_pizza = ["Pepperoni", "Cheese", "Hawaii", 42]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza
                           )

