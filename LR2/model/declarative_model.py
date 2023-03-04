from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql


Base = declarative_base()


class Student(Base):

    __tablename__ = 'students'

    student_id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    first_name = sql.Column(sql.String(100), nullable=False)
    last_name = sql.Column(sql.String(100), nullable=False)
    middle_name = sql.Column(sql.String(100), nullable=True)
    group_number = sql.Column(sql.String(10), nullable=True)
    illness_hours = sql.Column(sql.SmallInteger, nullable=False, default=0)
    other_hours = sql.Column(sql.SmallInteger, nullable=False, default=0)
    bad_hours = sql.Column(sql.SmallInteger, nullable=False, default=0)
    all_hours = sql.Column(sql.SmallInteger, nullable=False, default=0)
