from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Standard, Class, ClassName, Instance, InstanceStandard
from database_setup import ClassTaken, InstanceMember, InstanceStandardGrade, Base, ClassStandard

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
    session.query(InstanceMember).delete()
    session.query(InstanceStandardGrade).delete()
    session.query(ClassStandard).delete()
    session.commit()


###############################
#  Object Creation Functions  #
###############################


def new_standard(name, desc):
    session.add(Standard(standard_name=name,
                         standard_desc=desc))
    session.commit()
    return session.query(Standard).filter(Standard.standard_name == name).filter(Standard.standard_desc == desc).first().__id__


def new_class(name, desc):
    session.add(Class(current_name=999999,
                      class_desc=desc))
    session.commit()
    created_class = session.query(Class).filter(Class.current_name == 999999).first()
    new_classname(created_class.__id__, True, name)
    created_classname = session.query(ClassName).filter(ClassName.class_id == created_class.__id__).first()
    created_class.current_name = created_classname.__id__
    session.commit()
    return created_class.__id__


def new_classname(class_id, active, name):
    session.add(ClassName(class_id=class_id,
                          active=active,
                          name=name))
    session.commit()


def new_instance(class_id, class_name_id, block, start_trimester, end_trimester, year):
    session.add(Instance(class_id=class_id,
                         className_id=class_name_id,
                         block=block,
                         start_trimester=start_trimester,
                         end_trimester=end_trimester,
                         year=year))
    session.commit()
    instance_id = session.query(Instance).filter(Instance.class_id == class_id).\
        filter(Instance.className_id == class_name_id).\
        filter(Instance.year == year).\
        filter(Instance.block == block).\
        filter(Instance.end_trimester == end_trimester).\
        filter(Instance.start_trimester == start_trimester).\
        first().__id__
    # Inherits standards to instance
    for standard in session.query(ClassStandard).filter(ClassStandard.class_id == class_id).all():
        new_instance_standard(standard.__id__, instance_id)
    return instance_id


def new_class_standard(standard_id, class_id):
    session.add(ClassStandard(standard_id=standard_id,
                              class_id=class_id))
    session.commit()


def new_instance_standard(standard_id, instance_id):
    session.add(InstanceStandard(standard_id=standard_id,
                                 instance_id=instance_id))
    session.commit()


def new_instance_member(instance_id, student_id):
    session.add(InstanceMember(instance_id=instance_id,
                               student_id=student_id))
    session.commit()


def instance_standard_grade(student_id, standard_id, instance_id, grade):
    session.add(InstanceStandardGrade(student_id=student_id,
                                      standard_id=standard_id,
                                      instance_id=instance_id,
                                      grade=grade))
    session.commit()


###############################
#  Get Information Functions  #
###############################

def dict_of_classes():
    response = {
        'classes': []
    }
    for __class__ in session.query(Class).all():
        response['classes'].append(dict_of_class_info(__class__.__id__))
    return response


def dict_of_class_info(class_id):
    __class__ = session.query(Class).filter(Class.__id__ == class_id).first()
    class_info = {
        'name': current_class_name(class_id),
        'id': class_id,
        'desc': __class__.class_desc
    }
    return class_info


def dict_of_instance_info(instance_id):
    __instance__ = session.query(Instance).filter(Instance.__id__ == instance_id).first()
    instance_info = {
        'class_id': __instance__.class_id,
        'className_id': __instance__.className_id,
        'name': get_name_from_class_name_id(__instance__.className_id),
        'block': __instance__.block,
        'start_trimester': __instance__.start_trimester,
        'end_trimester': __instance__.end_trimester,
        'year': __instance__.year,
        'instance_id': __instance__.__id__
    }
    return instance_info


def dict_of_class_instances(class_id):
    response = {
        'instances': []
    }
    for __instance__ in session.query(Instance).filter(Instance.class_id == class_id).all():
        response['instances'].append(dict_of_instance_info(__instance__.__id__))
    return response


def current_class_name_id(class_id):
    return session.query(ClassName).filter(ClassName.class_id == class_id).filter(ClassName.active == True).first().__id__


def current_class_name(class_id):
    return session.query(ClassName).filter(ClassName.class_id == class_id).filter(ClassName.active == True).first().name


def get_name_from_class_name_id(class_name_id):
    return session.query(ClassName).filter(ClassName.__id__ == class_name_id).first().name


def dict_instances_with_student(student_id):
    response = {
        'instances': []
    }
    for __instance_member__ in session.query(InstanceMember).filter(InstanceMember.student_id == student_id).all():
        response['instances'].append(dict_of_instance_info(__instance_member__.instance_id))
    return response


def dict_instance_standards(instance_id):
    response = {
        'standards': []
    }
    for __instance_standard__ in session.query(InstanceStandard).filter(InstanceStandard.instance_id == instance_id).all():
        response['standards'].append(dict_standard_info(__instance_standard__.standard_id))
    return response


def dict_class_standards(class_id):
    response = {
        'standards': []
    }
    for __class_standard__ in session.query(ClassStandard).filter(ClassStandard.class_id == class_id).all():
        response['standards'].append(dict_standard_info(__class_standard__.standard_id))
    return response


def dict_standard_info(standard_id):
    __standard__ = session.query(Standard).filter(Standard.__id__ == standard_id).first()
    standard_info = {
        'name': __standard__.standard_name,
        'desc': __standard__.standard_desc,
        'standard_id': __standard__.__id__
    }
    return standard_info
