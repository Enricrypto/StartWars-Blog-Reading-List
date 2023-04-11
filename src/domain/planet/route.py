from flask import request, jsonify
from models.index import db, Planet
import domain.planet.controller as Controller 

def planet_route(app):

    @app.route('/planet', methods=['GET'])
    def get_all_planets():
        return Controller.get_all_planets() 

    @app.route('/planet', methods=['POST'])
    def create_planet():
        body = request.get_json()
        return Controller.create_planet(body) 
        
    @app.route('/planet/<int:id>', methods=['GET'])
    def get_planet_by_id(id):
        return Controller.get_planet_by_id(id)
        
