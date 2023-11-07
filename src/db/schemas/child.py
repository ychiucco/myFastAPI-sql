from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from .base_class import Base


class Child(Base):
    __tablename__ = "child"
    name: Mapped[str]    