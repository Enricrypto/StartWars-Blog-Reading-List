from models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    username = db.Column(db.String(150), unique= True, nullable=False)
    favorite = db.relationship("Favorite", back_populates='user')

    def __init__(self, id, email, username, is_active, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.is_active = True

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username, 
            "password": self.password,
            "active": self.is_active,
            "favorite": list(map(lambda  favorite: favorite.serialize_populate(), self.favorite))
        }
    
    def serialize_populate(self):
        return {
            "id": self.id,
            "username": self.username, 
        }