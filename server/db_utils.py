from models import db, Character

def get_all_characters():
    return db.session.query(Character).all()
