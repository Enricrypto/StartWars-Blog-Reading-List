import domain.people.repository as Repository
import handle_response as Response

def get_all_people():
    all_people = Repository.get_all_people()
    return Response.response_ok(all_people)

def create_people(data):
    if data['people_name'] is None or data['people_name'] == '':
        return Response.response_error( 'people_name not valid', 400)

    if data['description'] is None or data['description'] == '':
        return Response.response_error( 'description not valid', 400)

    if data['eye_color'] is None or data['eye_color'] == '':
        return Response.response_error( 'eye_color not valid', 400)

    return Repository.create_people(data), 201

def get_people_by_id(people_id):
    people = Repository.get_people_by_id(people_id)

    if people is None:
        return Response.response_error( 'people not found', 404)

    return people, 201

def delete_people(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404)
    people = Repository.delete_people(id) 
    if people is not None:
        return Response.response_ok("People deleted") 
    else:
        return Response.response_error("Id not found", 404)