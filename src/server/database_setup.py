import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import config

Base = declarative_base()


class Standard(Base):
    __tablename__ = 'Standard'
    __id__ = Column(Integer, primary_key=True)
    standard_name = Column(String(), nullable=False)
    standard_desc = Column(String(), nullable=False)


class Class(Base):
    __tablename__ = 'Class'
    __id__ = Column(Integer, primary_key=True)
    current_name = Column(Integer(), nullable=False)
    class_desc = Column(String(), nullable=False)


# We have to have a table to keep track of class names because people can't stop renaming classes.
class ClassName(Base):
    __tablename__ = 'ClassName'
    __id__ = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    name = Column(String(), nullable=False)


# Couldn't come up for a better name for a class session.
class Instance(Base):
    __tablename__ = 'Instance'
    __id__ = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    className_id = Column(Integer, nullable=False)
    block = Column(String(), nullable=False)
    start_trimester = Column(Integer, nullable=False)  # 1 for first trimester in a school year, 2 for second...
    end_trimester = Column(Integer, nullable=False)  # For most instances this will be the same as the start_trimester
    year = Column(Integer, nullable=False)  # The start of the school year (2015 for 2015-2016 school year


class InstanceStandard(Base):
    __tablename__ = 'InstanceStandard'
    __id__ = Column(Integer, primary_key=True)
    standard_id = Column(Integer, nullable=False)
    instance_id = Column(Integer, nullable=False)


class ClassStandard(Base):
    __tablename__ = 'ClassStandard'
    __id__ = Column(Integer, primary_key=True)
    standard_id = Column(Integer, nullable=False)
    class_id = Column(Integer, nullable=False)


class ClassTaken(Base):
    __tablename__ = 'ClassTaken'
    __id__ = Column(Integer, primary_key=True)
    instance_id = Column(Integer, nullable=False)  # The id of the instance
    student_id = Column(Integer, nullable=False)


class Student(Base):
    __tablename__ = 'Student'
    __id__ = Column(Integer, primary_key=True)
    student_id = Column(Integer)  # The user id obtained from google oauth
    avatar = Column(String())
    active = Column(Boolean, default=False)
    tokens = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())


# Table connecting the grades a student got for a standard in a class.
class ClassStandardGrade(Base):
    __tablename__ = 'ClassStandardGrade'
    __id__ = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    class_taken_id = Column(Integer)
    grade = Column(String())


# Create an engine that stores data in the local directory's
# database.db file.
engine = create_engine(config.path_to_database)  # In memory of Peter B.

Base.metadata.create_all(engine)