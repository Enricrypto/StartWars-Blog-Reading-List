from models.index import db, Planet

def get_all_planets():
    all_planets = Planet.query.all() 
    serialize_all_planets = [planet.serialize() for planet in all_planets]
    return serialize_all_planets

def create_planet(data):
    new_planet = Planet(data['color'], data['climate'], data['longitude'])
    db.session.add(new_planet)
    db.session.commit()
    return new_planet.serialize()

def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    return planet.serialize()



# @app.route('/planet/<int:id>', methods=['DELETE'])
# def delete_planet(id):
#     del_planet = People.query.get(id)
#     db.session.delete(del_planet)
#     db.session.commit()
#     return jsonify(del_planet.serialize()), 200