from datetime import datetime

from app import app

# JSON integration
@app.route('/date')
def get_current_date():
    favorite_pizza = {
        "John": "Pepperoni",
        "Mary": "Mushrooms",
        "Tim": "Hawaii",
        "Date": datetime.today()
    }
    return favorite_pizza
    # return {"Date": datetime.today()}
