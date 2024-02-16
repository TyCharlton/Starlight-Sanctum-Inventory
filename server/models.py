from config import db
from sqlalchemy.sql import func

class Character(db.Model):
    __tablename__ = "characters"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = func.now())
    updated_at = db.Column(db.DateTime, onupdate = func.now())
    def repr(self):
        return f"Character name: {self.name} Born: {self.created_at}"


class Inventory(db.Model):
    __tablename__ = "inventories"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    created_at = db.Column(db.DateTime, server_default = func.now())
    updated_at = db.Column(db.DateTime, onupdate = func.now())
    def repr(self):
        return f"Item name: {self.item} Picked up: {self.created_at} {self.character_id}"
    

    
