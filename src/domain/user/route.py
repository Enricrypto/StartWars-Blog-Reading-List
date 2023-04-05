from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller 

#la route llama al controller, donde está nuestra lógica

def user_route(app):

    @app.route('/user', methods=['POST'])
    def create_user():
        body = request.get_json()
        data, status = Controller.create_user(body)
        return jsonify(data), status
        
    @app.route('/user', methods=['GET'])
    def get_all_users(): 
        data, status = Controller.get_all_users() 
        return jsonify(data), status

    # @app.route('/user/favorites', methods = ['GET'])
    # def get_user_favorites():
    #     user_favorites = User.favorites.query.get()
    #     return jsonify(user_favorites.serialize()), 200