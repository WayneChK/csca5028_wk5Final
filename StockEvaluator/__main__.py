from StockEvaluator.AppServer import App
from StockEvaluator.SQLdb import sqlite_db

# Define a function to create the app
def create_app():
    with App.app.app_context():
        sqlite_db.db.create_all()
    return App.app

# The following line is required by Gunicorn
app = create_app()

# This line is for Python -m StockEvaluator
if __name__ == "__main__":
    app.run()

