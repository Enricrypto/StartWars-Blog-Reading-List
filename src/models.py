from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    username = db.Column(db.String(150), unique= True, nullable=False)
    favorites = db.relationship("Favorites")

    def __init__(self, email, username, is_active, password):
        # self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.is_active = True

    def serialize(self):
        return {
            # "id": self.id,
            "email": self.email,
            "username": self.username, 
            "password": self.password,
            "active": self.is_active
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(250))
    description = db.Column(db.String(250))
    eye_color =db.Column(db.String(250))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet")
    favorites = db.relationship("Favorites")

    def __init__(self, people_name, description, eye_color):
        self.people_name = people_name
        self.description = description
        self.eye_color = eye_color

    def serialize(self):
        return {
            "people_name": self.people_name,
            "description": self.description, 
            "eye_color": self.eye_color
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    longitude =db.Column(db.String(250))
    favorites = db.relationship("Favorites")

    def __init__(self, color, climate, longitude):
        self.color = color
        self.climate = climate
        self.longitude = longitude

    def serialize(self):
        return {
            "color": self.color,
            "climate": self.climate, 
            "longitude": self.longitude
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    people_id = db.Column(db.Integer,db.ForeignKey("people.id"))
    planet_id = db.Column(db.Integer,db.ForeignKey("planet.id"))
    user = db.relationship("User", back_populates = "favorites")
    planet = db.relationship("Planet", back_populates = "favorites")
    people = db.relationship("People", back_populates = "favorites")
   
    def __init__(self, user_id, people_id, planet_id):
        self.user_id = user_id
        self.people_id = people_id
        self.planet_id = planet_id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "people_id": self.people_id, 
            "planet_id": self.planet_id
        }