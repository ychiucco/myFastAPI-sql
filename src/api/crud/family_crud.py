from pydantic import BaseModel

# Parent CRUD

class ParentCreate(BaseModel):
    name: int

class ParentRead(BaseModel):
    id: int
    name: str
    children_ids: list[int] | None

class ParentUpdate(BaseModel):
    name: int

# Child CRUD

class ChildCreate(BaseModel):
    name: int
    parent_id: int

class ChildRead(BaseModel):
    id: int
    parent_id: int

class ChildUpdate(BaseModel):
    name: int
    parent_id: int