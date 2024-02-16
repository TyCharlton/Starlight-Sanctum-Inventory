from models import db, Character, Inventory


def get_all_characters():
    return db.session.query(Character).all()

def get_all_inventories():
    return db.session.query(Inventory).all()

def find_character_by_name(name):
    return db.session.query(Character).filter(Character.name == name).first()

def add_item_to_inventory(character):
    pass
