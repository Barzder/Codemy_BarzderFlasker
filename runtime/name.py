from flask import render_template, flash

from runtime import app
from webforms.namer_form import NamerForm

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash(u'Form Submitted Successfully!','success')
    return render_template('name.html',
        name = name,
        form = form
        )
