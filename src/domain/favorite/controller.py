from flask import request, jsonify
import domain.favorite.repository as Repository

def create_favorite(category, body):
    if category == 'planet':
        favorite_planet = Repository.create_favorite_planet(body)
        return favorite_planet.serialize_planet()
    else: 
        favorite_people = Repository.create_favorite_people(body)
        return favorite_people.serialize_people()

def delete_favorite(category, id):
    if category == 'people':
        favorite_people = Repository.delete_favorite_people(id)
        return favorite_people
    else: 
        favorite_planet = Repository.delete_favorite_planet(id)
        return favorite_planet

def get_fav():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_fav()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg

