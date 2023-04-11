from models.db import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    longitude =db.Column(db.String(250))
    favorite = db.relationship("Favorite", back_populates='planet')

    def __init__(self, color, climate, longitude):
        self.color = color
        self.climate = climate
        self.longitude = longitude

    def serialize(self):
        return {
            "id": self.id,
            "color": self.color,
            "climate": self.climate, 
            "longitude": self.longitude
        }