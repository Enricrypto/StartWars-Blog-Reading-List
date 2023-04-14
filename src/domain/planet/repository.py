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


def delete_planet(id):
    planet = Planet.query.get(id)
    if planet is None:  
        return planet  
    else:
        db.session.delete(planet)
        db.session.commit()
    return planet