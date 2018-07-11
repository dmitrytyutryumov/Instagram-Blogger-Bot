from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from etc.constants import DB_URL

engine = create_engine(DB_URL, module=sqlite)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


class BaseModel(Base):
    __abstract__ = True

    def save(self):
        db_session.add(self)
        try:
            db_session.commit()
        except:
            db_session.rollback()
        return self
