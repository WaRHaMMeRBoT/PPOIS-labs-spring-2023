import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
import os


# metadata = sql.MetaData()
#
# students = sql.Table('students', metadata,
#                      sql.Column('student_id', sql.Integer, primary_key=True),
#                      sql.Column('first_name', sql.String(100), nullable=False),
#                      sql.Column('last_name', sql.String(100), nullable=False),
#                      sql.Column('middle_name', sql.String(100), nullable=True),
#                      sql.Column('group_number', sql.String(10), nullable=True),
#                      sql.Column('illness_hours', sql.SmallInteger, nullable=False),
#                      sql.Column('other_hours', sql.SmallInteger, nullable=False),
#                      sql.Column('bad_hours', sql.SmallInteger, nullable=False),
#                      sql.Column('all_hours', sql.SmallInteger, nullable=False)
#                      )
#
# engine = sql.engine.create_engine('sqlite:///students.db', echo=True)
# metadata.create_all(engine)


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
