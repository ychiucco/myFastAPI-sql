from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Mapped
from .base_class import Base

class School(Base):
    __tablename__ = "school"
    name: Mapped[str]
    adress: Mapped[str]

    students: Mapped[list["Student"]] = relationship(back_populates="school")
    teachers: Mapped[list["Teacher"]] = relationship(back_populates="school")