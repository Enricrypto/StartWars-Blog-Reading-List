from models.index import db, User
from domain.favorite.repository import delete_all_favorites

# en el repository están las queries (funciones) que llaman a los modelos (models)
# para registrar, verificar o guardar información en la base de datos

def create_user(data):  
    new_user = User(data['email'], data['username'], data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_all_users(): 
    users = User.query.all()
    serialize_all_users = list(map(lambda user: user.serialize_user(), users))
    # serialize_all_users = [user.serialize() for user in users] ==> This is the same as above, an array comprehension
    return serialize_all_users

def get_user_by_id(id):
    user = User.query.get(id)
    return user.serialize()

def delete_user(id):
    user = User.query.get(id)
    if user is None:  # si el usuario viene vacio
        return user  # retorno la variable como none
    else:
        delete_all_favorites(user.id) 
        #se borran los favoritos antes de borrar el propio usuario, para poder hacer esto hay que importarlo arriba
        db.session.delete(user)
        db.session.commit()
    return user
