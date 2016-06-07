from app import app_
from flask import jsonify
import database_functions


@app_.errorhandler(404)
def page_not_found(e):
    return "404 page not found."


@app_.route('/')
def index():
    return 'Hello World!'


@app_.route('/classes/list')
def classes_list():
    response = database_functions.dict_of_classes()
    return jsonify(**response)


@app_.route('/<int:class_id>/info')
def class_info(class_id):
    response = database_functions.dict_of_class_info(class_id)
    return jsonify(**response)
