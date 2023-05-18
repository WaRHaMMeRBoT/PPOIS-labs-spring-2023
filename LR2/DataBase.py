from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


class Tournament(Base):
    __tablename__ = "tournament"
    id = Column(Integer, primary_key=True, index=True)
    tournament_name = Column(String)
    date = Column(String)
    sport_name = Column(String)
    winner_name = Column(String)
    prize_money = Column(Integer, )
    winner_money = Column(Integer, )


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


