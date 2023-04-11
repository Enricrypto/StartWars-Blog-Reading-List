from models.index import db, People

def get_all_people():
    all_people = People.query.all() 
    serialize_all_people = [people.serialize() for people in all_people]
    return serialize_all_people

def create_people(data):
    new_people = People(data['people_name'], data['description'], data['eye_color'])
    db.session.add(new_people)
    db.session.commit()
    return new_people.serialize()

def get_people_by_id(people_id):
    people = People.query.get(people_id)
    return people.serialize()