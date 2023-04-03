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
from models import db, User, People, Planet

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

# ENDPOINTS

# USER 
@app.route('/users', methods=['GET'])
def get_all_users(): 
    all_users = User.query.all()
    serialize_all_users = list(map(lambda user: user.serialize(), all_users))
    return jsonify(serialize_all_users), 200

@app.route('/users/favorites', methods = ['GET'])
def get_user_favorites():
    user_favorites = User.favorites.query.get()
    return jsonify(user_favorites.serialize()), 200

#PEOPLE
@app.route('/people', methods=['GET'])
def get_all_people():
    all_people= People.query.all() 
    serialize_all_people = [people.serialize() for people in all_people] 
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
    serialize_all_planets = [planet.seralize() for planet in all_planets]
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


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
