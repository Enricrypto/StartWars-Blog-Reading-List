from models.index import db, User

def create_user(): 
    new_user = User(data['email'], data['username'], data['password'], data['is_active'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_all_users(): 
    all_users = User.query.all()
    serialize_all_users = list(map(lambda user: user.serialize(), all_users))
    return serialize_all_users
