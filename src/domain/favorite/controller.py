from flask import request, jsonify
import domain.favorite.repository as Repository

def create_favorite(category, body):
    if category == 'planet':
        favorite_planet = Repository.create_favorite_planet(body)
        return favorite_planet.serialize_planet()
    else: 
        favorite_people = Repository.create_favorite_people(body)
        return favorite_people.serialize_people()
