from config import app, migrate
from rich import print
from db_utils import get_all_characters, find_character_by_name, add_item_to_inventory, get_all_inventories
from models import db, Character, Inventory


def display_welcome_message():
  print("""
  _________ __               .__  .__       .__     __      _________                     __                 
 /   _____//  |______ _______|  | |__| ____ |  |___/  |_   /   _____/____    ____   _____/  |_ __ __  _____  
 \_____  \\   __\__  \\_  __ \  | |  |/ ___\|  |  \   __\  \_____  \\__  \  /    \_/ ___\   __\  |  \/     \ 
 /        \|  |  / __ \|  | \/  |_|  / /_/  >   Y  \  |    /        \/ __ \|   |  \  \___|  | |  |  /  Y Y  \\
/_______  /|__| (____  /__|  |____/__\___  /|___|  /__|   /_______  (____  /___|  /\___  >__| |____/|__|_|  /
        \/           \/             /_____/      \/               \/     \/     \/     \/                 \/ 
""")


def display_main_menu():
  print("[bold green]Main Menu:[bold green/][green/]")
  print("[bold green]1. Create a new character.[bold green/][green/]")
  print("[bold green]2. List all characters.[bold green/][green/]")
  print("[bold green]3. Exit.[bold green/][green/]")
  print("[bold red]4. Delete Character.[bold red/][red/]")
  

def get_main_choice():
  return input("Enter your choice: ")

def display_all_characters():
    characters = get_all_characters()
    for character in characters:
      print(f"{character.name}")
    print("[bold green]What would you like to do?[bold green/]")
    print("[bold green]1. See Character's info.[green/]")
    print("[bold green]2. Return to main menu.[bold green/]")
    print("[bold green]3. Exit.[bold green/][green/]")
    choice = input("Enter your choice: ")
    if choice == "1":
      choose_character_by_name()
    else:
      return 
    
def choose_character_by_name():
  search_name = input("Enter the name of the character you would like to see: ")
  character = find_character_by_name(search_name)
  if character is not None:
    print(
      f"Id: {character.id} Character name: {character.name} Born: {character.created_at}"
        )
  else:
    print("Character not found.")
  display_character_menu(character)

def display_character_menu(character):
  print("[bold green]Inventory:[bold green/][green/]")
  print("[bold green]1. See Character's inventory.[bold green/][green/]")
  print("[bold green]2. Add item to inventory. [bold green/][green/]")
  print("[bold green]3. Drop item from inventory. [bold green/][green/]")
  print("[bold green]4. Change characters name. [bold green/][green/]")
  print("[bold green]5. Return to main menu.[bold green/][green/]")
  print("[bold green]6. Exit.[bold green/][green/]")
  choice = input("Enter your choice: ")
  if choice == "1":
    display_character_inventory(character)
  elif choice == "2":
    add_item_to_inventory(character, input("Enter the item you would like to add: "))
  elif choice == "3":
    delete_item_from_inventory(character, input("Enter the item you would like to drop: "))
  elif choice == "4":
    new_name = input("Enter the new name for your character: ")
    change_character_name(character, new_name)
  elif choice == "5":
    display_main_menu()
  elif choice == "6":
    print("[bold green]Exiting the app.[bold green/][green/]")
    exit()
  else:
    print("[bold red]Invalid choice.[bold red/][red/]")


def display_character_inventory(character):
  inventory_items = Inventory.query.filter_by(character_id=character.id).all()
  if inventory_items:
    print(f"{character.name}'s Inventory:")
    for item in inventory_items:
     print(f"- {item.item}")
  else:
     print(f"{character.name}'s inventory is empty.")


def add_item_to_inventory(character, item_name):
  inventory = Inventory(
    character_id=character.id,
    item=item_name
  )
  db.session.add(inventory)
  db.session.commit()
  print(f"Added {item_name} to {character.name}'s inventory.")

def delete_item_from_inventory(character, item_name):
  inventory_item = Inventory.query.filter_by(character_id=character.id, item=item_name).first()
  if inventory_item:
    db.session.delete(inventory_item)
    db.session.commit()
    print(f"Deleted {item_name} from {character.name}'s inventory.")
  else:
    print(f"{character.name} does not have {item_name} in their inventory.")

def change_character_name(character, new_name):
    character.name = new_name
    db.session.commit()
    print(f"Changed {character.name}'s name to {new_name}.")


def create_new_character(name):
    new_character = Character(name=name)
    db.session.add(new_character)
    db.session.commit()
    print(f"Created new character: {new_character.name}")

def delete_character(character):
    db.session.delete(character)
    db.session.commit()
    print(f"Deleted character: {character.name}")


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
        name = input("Enter the name of the new character: ")
        create_new_character(name)
        print("[bold green]Creating a new character.[bold green/][green/]")
      elif choice == "2":
        print(display_all_characters())
      elif choice == "3":
       print("[bold green]Exiting the app.[bold green/][green/]")
       exit()
      elif choice == "4":
        character_name = input("Enter the name of the character you would like to delete: ")
        character = find_character_by_name(character_name)
        if character:
         delete_character(character)
        break
      else:
        print("[bold red]Invalid choice.[bold red/][red/]")


        
      
      