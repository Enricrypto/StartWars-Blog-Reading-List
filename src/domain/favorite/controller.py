import domain.favorite.repository as Repository
import handle_response as Response

def create_favorite(category, body):
    if category == 'planet':
        favorite_planet = Repository.create_favorite_planet(body)
        return favorite_planet.serialize_planet()
    else: 
        favorite_people = Repository.create_favorite_people(body)
        return favorite_people.serialize_people()

def get_all_favorites():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    favorites = Repository.get_all_favorites()
    return Response.response_ok(favorites) #se utiliza la variable resultado para pasarla a response y que devuelva un msg

def delete_favorite(id):
        favorite = Repository.delete_favorite(id)
        return Response.response_ok("favorito eliminado")

def delete_all_favorites(user_id):
    if not isinstance(user_id, int):
        return Response.response_error("Id not found", 404)
    
    resultado = Repository.delete_all_favorites(user_id)
    return Response.response_ok("all favorites were deleted")