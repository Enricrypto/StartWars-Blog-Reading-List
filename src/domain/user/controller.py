import domain.user.repository as Repository
import handle_response as Response

def create_user(data):
    if data['email'] is None or data['email'] == '':
        return Response.response_error( 'Email not valid', 400)
    
    if data['username'] is None or data['username'] == '':
        return Response.response_error( 'user not valid', 400)
    
    return Repository.create_user(data), 201