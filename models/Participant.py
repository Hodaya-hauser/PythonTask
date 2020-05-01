from models.db import db
from sqlalchemy.ext.hybrid import hybrid_property


class Participant(db.Model):
    __tablename__ = 'Participant'
    participant_name = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    
    def __init__(self, participant_name):
        self.participant_name = participant_name

    def validation(self):
        if self.participant_name=="" or not self.participant_name:
            return {"message": "no participant provided"}, 400
        return None