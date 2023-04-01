import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os


if not database_exists('sqlite:///students.db'):
    create_database('sqlite:///students.db')


metadata = sql.MetaData()
students = sql.Table('students', metadata,
                    sql.Column('student_id', sql.Integer, primary_key=True),
                    sql.Column('first_name', sql.String(100), nullable=False),
                    sql.Column('last_name', sql.String(100), nullable=False),
                    sql.Column('middle_name', sql.String(100), nullable=True),
                    sql.Column('year', sql.SmallInteger, nullable=False),
                    sql.Column('group_number', sql.String(10), nullable=False),
                    sql.Column('all_assignments', sql.SmallInteger, nullable=True),
                    sql.Column('completed_assignments', sql.SmallInteger, nullable=True),
                    sql.Column('language', sql.String(100), nullable=False)
                    )

class DbConnect:
    def __init__(self) -> None:
        self.engine = sql.create_engine('sqlite:///db/students.db', echo=True)
        try:
            self.engine.connect()
            metadata.create_all(self.engine, checkfirst=True) 
        except SQLAlchemyError:
            print('No connection to database.\nCheck availability of database\n'
                  'and try again')
            raise SQLAlchemyError

    def session(self):
        return sessionmaker(bind=self.engine)
