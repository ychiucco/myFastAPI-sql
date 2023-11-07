from sqlalchemy import exc
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.congif import get_settings

settings = get_settings()
engine = create_engine(
    settings.POSTGRES_URL, connect_args={"check_same_thread": False}
)

def get_db():
    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
