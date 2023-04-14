from flask import request, jsonify
from models.index import db, People
import domain.people.controller as Controller 

def people_route(app):

    @app.route('/people', methods=['GET'])
    def get_all_people():
        return Controller.get_all_people() 
    
    @app.route('/people', methods=['POST'])
    def create_people():
        body = request.get_json()
        return Controller.create_people(body) 

    @app.route('/people/<int:id>', methods=['GET'])
    def get_people_by_id(id):
        return Controller.get_people_by_id(id)

    @app.route('/people/<int:id>', methods=['DELETE'])
    def delete_people(id):
        return Controller.delete_people(id)