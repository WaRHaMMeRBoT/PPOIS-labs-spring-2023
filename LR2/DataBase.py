from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


class Person(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    person_name = Column(String)
    date = Column(String)
    ill_hours = Column(String)
    other_reason = Column(String)
    no_reason = Column(String)
    all_hours = Column(Integer, )


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


