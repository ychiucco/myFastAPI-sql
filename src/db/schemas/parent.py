from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from .base_class import Base

class Parent(Base):
    __tablename__ = "parent"
    name: Mapped[str]