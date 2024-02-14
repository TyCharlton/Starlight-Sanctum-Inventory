from config import app, migrate
from rich import print

from models import db

def display_welcome_message():
  print("Welcome to my app. This will be changed.")

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    

    display_welcome_message()
