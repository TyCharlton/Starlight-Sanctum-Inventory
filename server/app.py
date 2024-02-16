from config import app, migrate
from rich import print
from db_utils import get_all_characters


from models import db

def display_welcome_message():
  print("[green]Welcome to my app. [bold Green]This will be changed.[bold green/][green/]")

def display_main_menu():
  print("[bold green]Main Menu:[bold green/][green/]")
  print("[bold green]1. Create a new character.[bold green/][green/]")
  print("[bold green]2. List all characters.[bold green/][green/]")
  print("[bold green]3. Exit.[bold green/][green/]")

def get_main_choice():
  return input("Enter your choice: ")

def display_all_characters():
  characters = get_all_characters()
  for character in characters:
    print(f"{character.name}")

if __name__ == "__main__":
  # gives app context at runtime to init migrate obj
  with app.app_context():
    migrate.init_app(app, db)
    

    display_welcome_message()
    while True:
      display_main_menu()
      choice = get_main_choice()
      print(choice)
      if choice == "1":
        print("[bold green]Creating a new character.[bold green/][green/]")
      elif choice == "2":
        print(display_all_characters())
      elif choice == "3":
        print("[bold green]Exiting the app.[bold green/][green/]")
        break
      else:
        print("[bold red]Invalid choice.[bold red/][red/]")


        
      
      