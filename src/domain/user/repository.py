from models.index import db, User

def create_user(): 
    new_user = User(data['email'], data['username'], data['password'], data['is_active'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()