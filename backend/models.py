from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    light = db.Column(db.String(50), nullable=False)
    water = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    care = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}