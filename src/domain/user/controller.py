import domain.user.repository as Repository
import handle_response as Response

#controller hará los llamados al repository y hará las validaciones

def create_user(data): #función importada desde el repository
    if data['email'] is None or data['email'] == '':
        return Response.response_error('Email not valid', 400)
    
    if data['username'] is None or data['username'] == '':
        return Response.response_error('user not valid', 400)
    
    return Repository.create_user(data), 201 #Nos devuelve la función del repositorio

def get_all_users():
    all_users = Repository.get_all_users()
    return Response.response_ok(all_users)

def get_user_by_id(user_id):
    user = Repository.get_user_by_id(user_id)

    if user is None:
        return Response.response_error('user not found', 404)
    
    return user

def delete_user(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404)
    user = Repository.delete_user(id) #usando como param el id 
    if user is not None:
        return Response.response_ok("User deleted") #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)
