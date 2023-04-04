from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller 

def user_route(app):

    @app.route('/user', methods=['POST'])
    def create_user():
        body = request.get_json()
        return Controller.create_user(body)