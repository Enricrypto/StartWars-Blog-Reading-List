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
from models.index import db, User, Planet, People, Favorite
from domain.user.route import user_route
from domain.planet.route import planet_route
from domain.people.route import people_route
from domain.favorite.route import favorite_route

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
planet = planet_route(app)
people = people_route(app)
favorite = favorite_route(app)



# @app.route('/people/<int:id>', methods=['DELETE'])
# def delete_people(id):
#     del_people = People.query.get(id)
#     db.session.delete(del_people)
#     db.session.commit()
#     return jsonify(del_people.serialize()), 200


# @app.route('/planet/<int:id>', methods=['DELETE'])
# def delete_planet(id):
#     del_planet = People.query.get(id)
#     db.session.delete(del_planet)
#     db.session.commit()
#     return jsonify(del_planet.serialize()), 200

#FAVORITE




if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
