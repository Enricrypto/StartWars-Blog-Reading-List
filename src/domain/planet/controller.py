import domain.planet.repository as Repository
import handle_response as Response

def get_all_planets():
    all_planets = Repository.get_all_planets()
    return Response.response_ok(all_planets)

def create_planet(data):
    if data['color'] is None or data['color'] == '':
        return Response.response_error( 'color not valid', 400)

    if data['climate'] is None or data['climate'] == '':
        return Response.response_error( 'climate not valid', 400)

    if data['longitude'] is None or data['longitude'] == '':
        return Response.response_error( 'longitude not valid', 400)
    
    return Repository.create_planet(data), 201

def get_planet_by_id(planet_id):
    planet = Repository.get_planet_by_id(planet_id)

    if planet is None:
        return Response.response_error( 'planet not found', 404)

    return planet, 201
