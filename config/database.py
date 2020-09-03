from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///..\\..\\persistent\\database.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def init():
    import models.database as database
    Base.metadata.create_all(engine)


def persistent(model):
    session.add(model)
    session.commit()
