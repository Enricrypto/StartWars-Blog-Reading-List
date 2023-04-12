from flask import request, jsonify
import domain.favorite.controller as Controller 

def favorite_route(app):

    @app.route('/favorite/<string:category>', methods = ['POST'])
    def create_favorite(category):
        # bring all variables at once
        body = request.get_json() 
        favorite = Controller.create_favorite(category, body)
        print(favorite)
        print(type(favorite))
        return jsonify(favorite), 201



# @app.route('/user/<int:user_id>/favorite/people', methods=['POST'])
# def add_favorite_people(user_id):
#     #obtener los datos del favorito
#     people_id = request.json.get('people_id', None)
#     #buscar el usuario en mi base de datos
#     user = User.query.get(user_id)
#     if user is None: 
#         return jsonify({'msg' : 'el usuario no existe'}), 401
    
#     favorite = Favorite(user_id = user_id, people_id = people_id)
#     db.session.add(favorite)
#     db.session.commit()
#     #obtener la lista actualizada de los favoritos del usuario
#     user_favorite = Favorite.query.filter_by(user_id = user_id).all()
#     all_user_favorites = [element.serialize() for element in user_favorite]
#     print(all_user_favorites)
#     response_body = {'msg' : 'favorito agregado', 'favoritos' : all_user_favorites}
#     return jsonify(response_body), 200
 