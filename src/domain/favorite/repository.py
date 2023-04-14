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

def get_all_favorites():
        favorites = Favorite.query.all()
        fav_serialized = list(map(lambda fav: fav.serialize_populate(), favorites)) 
        # se llama a la funcion que serializa todo excepto el otro mapeo
        return fav_serialized

def delete_favorite(id):
    favorite = Favorite.query.get(id)
    if favorite is None:
        return favorite
    else:
        db.session.delete(favorite)
        db.session.commit()
    return favorite

def delete_all_favorites(user_id):
    favorites = Favorite.query.filter_by(user_id=user_id).first()
    db.session.delete(favorites)
    db.session.commit()
    return favorites

