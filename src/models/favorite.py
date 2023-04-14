from models.db import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    people_id = db.Column(db.Integer,db.ForeignKey("people.id"))
    planet_id = db.Column(db.Integer,db.ForeignKey("planet.id"))
    user = db.relationship("User", back_populates = "favorite")
    planet = db.relationship("Planet", back_populates = "favorite")
    people = db.relationship("People", back_populates = "favorite")
   
    def __init__(self, people_id, planet_id, user_id):
        self.people_id = people_id
        self.planet_id = planet_id
        self.user_id = user_id

    def serialize_people(self):
        return {
            "id": self.id, 
            "user_id": self.user_id,
            "people_id": self.people_id, 
            "user":  self.user.serialize(),
            "people": self.people.serialize() 
        }
    
    def serialize_planet(self):
        return {
            "id": self.id, 
            "user_id": self.user_id,
            "planet_id": self.planet_id, 
            # "user":  self.user.serialize(),
            # "planet": self.planet.serialize() 
        }
    
    def serialize_populate(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }