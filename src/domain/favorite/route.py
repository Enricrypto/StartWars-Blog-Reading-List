from flask import request, jsonify
import domain.favorite.controller as Controller 
from models.index import db, Favorite

def favorite_route(app):

    @app.route('/favorite/<string:category>', methods = ['POST'])
    def create_favorite(category):
        # bring all variables at once
        body = request.get_json() 
        favorite = Controller.create_favorite(category, body)
        return jsonify(favorite), 201

    @app.route('/favorite', methods = ['GET'])
    def get_all_favorites():
        return Controller.get_all_favorites()

    @app.route('/favorite/<string:category>/<int:id>', methods=['DELETE'])
    def delete_favorite(category, id): 
        return Controller.delete_favorite(category, id)

