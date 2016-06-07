from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Standard, Class, ClassName, Instance, InstanceStandard
from database_setup import ClassTaken, Student, ClassStandardGrade, Base, ClassStandard

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
    session.query(ClassStandard).delete()
    session.commit()


def new_student(student_id, avatar, active, tokens):
    session.add(Student(student_id=student_id, avatar=avatar, active=active, tokens=tokens))
    session.commit()


def new_standard(name, desc):
    session.add(Standard(standard_name=name, standard_desc=desc))
    session.commit()
    return session.query(Standard).filter(Standard.standard_name == name).filter(Standard.standard_desc == desc).first().__id__


def new_class(name, desc):
    session.add(Class(current_name=999999, class_desc=desc))
    session.commit()
    created_class = session.query(Class).filter(Class.current_name == 999999).first()
    new_classname(created_class.__id__, True, name)
    created_classname = session.query(ClassName).filter(ClassName.class_id == created_class.__id__).first()
    created_class.current_name = created_classname.__id__
    session.commit()
    return created_class.__id__


def current_class_name_id(class_id):
    return session.query(ClassName).filter(ClassName.class_id == class_id and ClassName.active == True).first().__id__


def new_classname(class_id, active, name):
    session.add(ClassName(class_id=class_id, active=active, name=name))
    session.commit()


def new_instance(class_id, className_id, block, start_trimester, end_trimester, year):
    session.add(Instance(class_id=class_id, className_id=className_id, block=block, start_trimester=start_trimester, end_trimester=end_trimester, year=year))
    session.commit()
    instance_id = session.query(Instance).filter(Instance.class_id == class_id).\
        filter(Instance.className_id == className_id).\
        filter(Instance.year == year).\
        filter(Instance.block == block).\
        filter(Instance.end_trimester == end_trimester).\
        filter(Instance.start_trimester == start_trimester).\
        first().__id__
    # Add standards to instance
    for standard in session.query(ClassStandard).filter(ClassStandard.class_id == class_id).all():
        new_instance_standard(standard.__id__, instance_id)
    return instance_id


def new_class_standard(standard_id, class_id):
    session.add(ClassStandard(standard_id=standard_id, class_id=class_id))
    session.commit()


def new_instance_standard(standard_id, instance_id):
    session.add(InstanceStandard(standard_id=standard_id, instance_id=instance_id))
    session.commit()
