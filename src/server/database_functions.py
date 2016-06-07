from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Standard, Class, ClassName, Instance, InstanceStandard, ClassTaken, Student, ClassStandardGrade, Base

from helper_functions import *

import uuid, time

import config

# Connects to the database
engine = create_engine(config.path_to_database)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def wipe_tables():
    session.query(Standard).delete()
    session.query(Class).delete()
    session.query(ClassName).delete()
    session.query(Instance).delete()
    session.query(InstanceStandard).delete()
    session.query(ClassTaken).delete()
    session.query(Student).delete()
    session.query(ClassStandardGrade).delete()
    session.commit()


def new_student(student_id, avatar, active, tokens):
    session.add(Student(student_id=student_id, avatar=avatar, active=active, tokens=tokens))
    session.commit()


def new_standard(name, desc):
    session.add(Standard(standard_name=name, standard_desc=desc))
    session.commit()


def new_class(name, desc):
    session.add(Class(current_name=999999, class_desc=desc))
    session.commit()
    created_class = session.query(Class).filter(Class.current_name == 999999).first()
    new_classname(created_class.__id__, True, name)
    created_classname = session.query(ClassName).filter(ClassName.class_id == created_class.__id__).first()
    created_class.current_name = created_classname.__id__
    session.commit()


def new_classname(class_id, active, name):
    session.add(ClassName(class_id=class_id, active=active, name=name))
    session.commit()
