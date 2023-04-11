from models.index import db, User

# en el repository están las queries (funciones) que llaman a los modelos (models)
# para registrar, verificar o guardar información en la base de datos

def create_user(data):  
    new_user = User(data['email'], data['username'], data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_all_users(): 
    users = User.query.all()
    serialize_all_users = list(map(lambda user: user.serialize(), users))
    return serialize_all_users

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user.serialize()