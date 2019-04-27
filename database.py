from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String


engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()



class philMed(Base):
	__tablename__ = "philMed"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime, default=datetime.datetime.utcnow)
    anxious = Column(Text, nullable=False)
    upset = Column(Text, nullable=False)
    excited = Column(Text, nullable=False)
Base.metadata.create_all(engine)

"""

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import philMed.models
    Base.metadata.create_all(engine)
"""
