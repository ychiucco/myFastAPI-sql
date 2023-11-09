from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .base_class import Base


class Student(Base):
    __tablename__ = "student"
    name: Mapped[str]
    age: Mapped[int]
    
    school_id: Mapped[int] = mapped_column(ForeignKey("school.id"))
    school: Mapped["School"] = relationship(back_populates="students")

class Teacher(Base):
    __tablename__ = "teacher"
    name: Mapped[str]

    school_id: Mapped[int] = mapped_column(ForeignKey("school.id"))
    school: Mapped["School"] = relationship(back_populates="teachers")