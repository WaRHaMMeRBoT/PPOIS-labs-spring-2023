import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker


class DbConnect:
    def __init__(self) -> None:
        self.engine = sql.create_engine('sqlite:///db/students.db', echo=True)
        try:
            self.engine.connect()
        except SQLAlchemyError:
            print('No connection to database.\nCheck availability of database\n'
                  'and try again')
            raise SQLAlchemyError

    def session(self):
        return sessionmaker(bind=self.engine)
