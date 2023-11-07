from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .api.crud.family_crud import ChildCreate
from .api.crud.family_crud import ChildRead
from .api.crud.family_crud import ParentCreate
from .api.crud.family_crud import ParentRead
from .api.crud.family_crud import ParentUpdate
from .db.schemas.parent import Child
from .db.schemas.parent import Parent
from .db.session import get_db

app = FastAPI()

@app.post("/parent/", response_model=ParentRead, status_code=201)
def create_parent(parent: ParentCreate, db: Session = Depends(get_db)):
    
    parent = Parent(name=parent.name)
    db.add(parent)
    db.commit()
    db.refresh(parent)
    return ParentRead(id=parent.id, name=parent.name)

@app.get("/parent/{id}", response_model=ParentRead, status_code=200)
def read_parent(id: int, db: Session = Depends(get_db)):
    
    parent = db.get(Parent, id)
    if parent is None:
        raise HTTPException(status_code=404, detail=f"Parent {id} not found")
    
    return ParentRead(
        id=parent.id,
        name=parent.name,
        children_ids=[
            child.id for child in parent.children
        ] if parent.children else [],
    )

@app.update("/parent/{id}", response_model=ParentRead, status_code=200)
def update_parent(
    id: int, update: ParentUpdate, db: Session = Depends(get_db)
):
    
    parent = db.get(Parent, id)
    if parent is None:
        raise HTTPException(status_code=404, detail=f"Parent {id} not found")
    
    parent.name = update.name
    db.add(parent)
    db.commit()
    db.refresh(parent)

    return ParentRead(
        id=parent.id,
        name=parent.name,
        children_ids=[
            child.id for child in parent.children
        ] if parent.children else [],
    )

@app.delete("/parent/{id}", status_code=204)
def delete_parent(id: int, db: Session = Depends(get_db)):

    parent = db.get(Parent, id)
    if parent is None:
        raise HTTPException(status_code=404, detail=f"Parent {id} not found")
    
    db.delete(parent)
    db.commit
    return
