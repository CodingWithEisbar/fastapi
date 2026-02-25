from sqlalchemy.orm import Session
import model
import schemas

# READ: Get a single item by ID
def get_item(db: Session, item_id: int):
    return db.query(model.Item).filter(model.Item.id == item_id).first()

# READ: Get a list of items
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Item).offset(skip).limit(limit).all()

# CREATE: Add a new item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = model.Item(title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# UPDATE: Update an existing item
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = get_item(db, item_id)
    if db_item:
        db_item.title = item.title
        db_item.description = item.description
        db.commit()
        db.refresh(db_item)
    return db_item

# DELETE: Remove an item
def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item