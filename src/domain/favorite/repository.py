from models.index import db, Favorite

def create_favorite_people(body):
    new_favorite = Favorite (body['people_id'], None, body['user_id'])
    db.session.add(new_favorite)
    db.session.commit()
    print(new_favorite)
    return new_favorite


def create_favorite_planet(body):
    new_favorite = Favorite (None, body['planet_id'], body['user_id'])
    db.session.add(new_favorite)
    db.session.commit()
    print(new_favorite)
    return new_favorite