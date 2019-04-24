# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Student(Base):
    __tablename__ = 'Student'

    studentid = Column(Integer, primary_key=True)
    studentname = Column(String(100))
    studentclass = Column(Integer)


class User(Base):
    __tablename__ = 'user'

    uid = Column(Integer, primary_key=True)
    uname = Column(String(20), nullable=False)
    uemail = Column(String(40))
