from app import app_
from flask import jsonify
import database_functions


@app_.errorhandler(404)
def page_not_found(e):
    return "404 page not found."


@app_.route('/')
def index():
    return 'Hello World!'


@app_.route('/classes/all/list')
def classes_list():
    response = database_functions.dict_of_classes()
    return jsonify(**response)


@app_.route('/classes/<int:class_id>/info')
def class_info(class_id):
    response = database_functions.dict_of_class_info(class_id)
    return jsonify(**response)


@app_.route('/classes/<int:class_id>/instances')
def class_instances(class_id):
    response = database_functions.dict_of_class_instances(class_id)
    return jsonify(**response)


@app_.route('/classes/<int:class_id>/standards')
def class_standards(class_id):
    response = database_functions.dict_class_standards(class_id)
    return jsonify(**response)


@app_.route('/classes/instances/<int:instance_id>/standards/list')
def instance_standards(instance_id):
    response = database_functions.dict_instance_standards(instance_id)
    return jsonify(**response)


@app_.route('/student/<int:student_id>/instances')
def student_instances(student_id):
    response = database_functions.dict_instances_with_student(student_id)
    return jsonify(**response)


@app_.route('/student/<int:student_id>/instances/all/grade')
def student_instance_grades(student_id):
    response = database_functions.dict_instances_grades(student_id)
    return jsonify(**response)


@app_.route('/student/<int:student_id>/instances/<int:instance_id>/grade')
def student_instance_grade(student_id, instance_id):
    response = database_functions.dict_instance_grades(student_id, instance_id)
    return jsonify(**response)
