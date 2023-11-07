from sqlalchemy import orm
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(orm.DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)