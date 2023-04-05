from models.db import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(250))
    description = db.Column(db.String(250))
    eye_color =db.Column(db.String(250))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet")
    favorite = db.relationship("Favorite")

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