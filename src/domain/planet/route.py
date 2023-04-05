from flask import request, jsonify
from models.index import db, Planet
import domain.planet.controller as Controller 

def planet_route(app):

    @app.route('/planet', methods=['GET'])
    def get_all_planets():
        return Controller.get_all_planets()


