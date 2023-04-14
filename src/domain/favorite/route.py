from flask import request, jsonify
import domain.favorite.controller as Controller 

def favorite_route(app):

    @app.route('/favorite/<string:category>', methods = ['POST'])
    def create_favorite(category):
        # bring all variables at once
        body = request.get_json() 
        favorite = Controller.create_favorite(category, body)
        return jsonify(favorite), 201

    @app.route('/favorite', methods = ['GET'])
    def get_all_favorites():
        fav_serialized = list(map(lambda fav: fav.serialize_planet(), get_all_favorites)) 
        # se llama a la funcion que serializa todo excepto el otro mapeo
        return jsonify(fav_serialized)

    @app.route('/favorite/<string:category>/<int:id>', methods=['DELETE'])
    def delete_favorite(category, id): 
        return Controller.delete_favorite(category, id)

