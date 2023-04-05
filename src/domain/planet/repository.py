from models.index import db, Planet


def get_all_planets():
    all_planets = Planet.query.all() 
    serialize_all_planets = [planet.serialize() for planet in all_planets]
    return serialize_all_planets

# @app.route('/planet/<int:id>', methods=['GET'])
# def get_planet(id):
#     planet = Planet.query.get(id)
#     return jsonify(planet.serialize()), 200

# @app.route('/planet', methods=['POST'])
# def create_planet():
#     data = request.get_json()
#     new_planet = Planet(data['color'], data['climate'], data['longitude'])
#     db.session.add(new_planet)
#     db.session.commit()
#     return jsonify(new_planet.serialize()), 200

# @app.route('/planet/<int:id>', methods=['DELETE'])
# def delete_planet(id):
#     del_planet = People.query.get(id)
#     db.session.delete(del_planet)
#     db.session.commit()
#     return jsonify(del_planet.serialize()), 200