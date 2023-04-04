"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models.index import db, User
from domain.user.route import user_route

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


user = user_route(app)



# USER 
@app.route('/user', methods=['GET'])
def get_all_users(): 
    all_users = User.query.all()
    serialize_all_users = list(map(lambda user: user.serialize(), all_users))
    return jsonify(serialize_all_users), 200

@app.route('/user', methods=['POST'])
def create_user(): 
    data = request.get_json()
    new_user = User(data['email'], data['username'], data['password'], data['is_active'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 200

# @app.route('/user/favorites', methods = ['GET'])
# def get_user_favorites():
#     user_favorites = User.favorites.query.get()
#     return jsonify(user_favorites.serialize()), 200

#PEOPLE
@app.route('/people', methods=['GET'])
def get_all_people():
    all_people = People.query.all() 
    serialize_all_people = list(map(lambda people: people.serialize(), all_people))
    return jsonify(serialize_all_people), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_people(id):
    people = People.query.get(id)
    return jsonify(people.serialize()), 200

@app.route('/people', methods=['POST'])
def create_people():
    data = request.get_json()
    new_people = People(data['people_name'], data['description'], data['eye_color'])
    db.session.add(new_people)
    db.session.commit()
    return jsonify(new_people.serialize()), 200

@app.route('/people/<int:id>', methods=['DELETE'])
def delete_people(id):
    del_people = People.query.get(id)
    db.session.delete(del_people)
    db.session.commit()
    return jsonify(del_people.serialize()), 200

#PLANETS
@app.route('/planet', methods=['GET'])
def get_all_planets():
    all_planets = Planet.query.all() 
    serialize_all_planets = [planet.serialize() for planet in all_planets]
    return jsonify(serialize_all_planets), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200

@app.route('/planet', methods=['POST'])
def create_planet():
    data = request.get_json()
    new_planet = Planet(data['color'], data['climate'], data['longitude'])
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(new_planet.serialize()), 200

@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet(id):
    del_planet = People.query.get(id)
    db.session.delete(del_planet)
    db.session.commit()
    return jsonify(del_planet.serialize()), 200

#FAVORITE
@app.route('/user/<int:user_id>/favorite/people', methods=['POST'])
def add_favorite_people(user_id):
    #obtener los datos del favorito
    people_id = request.json.get('people_id', None)
    #buscar el usuario en mi base de datos
    user = User.query.get(user_id)
    if user is None: 
        return jsonify({'msg' : 'el usuario no existe'}), 401
    favorite = Favorite(user_id = user_id, people_id = people_id)
    db.session.add(favorite)
    db.session.commit()
    #obtener la lista actualizada de los favoritos del usuario
    user_favorite = Favorite.query.filter_by(user_id = user_id).all()
    all_user_favorites = [element.serialize() for element in user_favorite]
    print(all_user_favorites)
    response_body = {'msg' : 'favorito agregado', 'favoritos' : all_user_favorites}
    return jsonify(response_body), 200

# @app.route('/favorite/people/<int:id>', methods=['POST'])
# def create_favorite_people(id):
#     data = request.get_json()
#     new_favorite_people = Favorite(data['people_id'])
#     return jsonify(new_favorite_people.serialize()), 200



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
