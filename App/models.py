from . import db

class PatientData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    ethnicity = db.Column(db.String(50), nullable=False)
    family_history = db.Column(db.String(3), nullable=False)
    radiation_exposure = db.Column(db.String(3), nullable=False)
    iodine_deficiency = db.Column(db.String(3), nullable=False)
    smoking = db.Column(db.String(3), nullable=False)
    obesity = db.Column(db.String(3), nullable=False)
    diabetes = db.Column(db.String(3), nullable=False)
    tsh_level = db.Column(db.Float, nullable=False)
    t3_level = db.Column(db.Float, nullable=False)
    t4_level = db.Column(db.Float, nullable=False)
    nodule_size = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Patient {self.id}>'
