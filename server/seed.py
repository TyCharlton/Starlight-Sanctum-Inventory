from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
    
    print("clearing out tables")

    Character.query.delete()
    Inventory.query.delete()

    print("seeding characters table")

    character1 = Character(
      name="Tyler"

    )

    db.session.add(character1)
    db.session.commit()

    character2 = Character(
      name="Nuburooj"

    )

    db.session.add(character2)
    db.session.commit()

    character3 = Character(
      name="Hussein"

    )

    db.session.add(character3)
    db.session.commit()

    print("seeding inventories table")

    inventory1 = Inventory(
      character_id=character1.id,
      item="Bow"

    )

    db.session.add(inventory1)
    db.session.commit()

    inventory2 = Inventory(
      character_id=character1.id,
      item="Sword"

    )

    db.session.add(inventory2)
    db.session.commit()

    inventory3 = Inventory(
      character_id=character3.id,
      item="2H Sword"

    )

    db.session.add(inventory3)
    db.session.commit()



    




