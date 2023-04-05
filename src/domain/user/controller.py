import domain.user.repository as Repository
import handle_response as Response

#controller hará los llamados al repository y hará las validaciones

def create_user(data): #función importada desde el repository
    if data['email'] is None or data['email'] == '':
        return Response.response_error( 'Email not valid', 400)
    
    if data['username'] is None or data['username'] == '':
        return Response.response_error( 'user not valid', 400)
    
    return Repository.create_user(data), 201 #Nos devuelve la función del repositorio

def get_all_users():
    
    return Repository.get_all_users(), 200