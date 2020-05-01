from models.db import db
from flask import jsonify
from models.Session import Session
from models.Participant import Participant
association_table = db.Table('association', 
    db.Column('left_id', db.String(255),db.ForeignKey('Message.message_id')),
    db.Column('participant_name', db.String(255), db.ForeignKey('Participant.participant_name'))
)

class Message(db.Model):
    __tablename__ = 'Message'
    application_id = db.Column(db.Integer, nullable=False)
    session_id = db.Column(db.String(255), db.ForeignKey("Session.session_id"),  nullable=False)
    message_id = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    participants = db.relationship("Participant",
                    secondary=association_table)
    content = db.Column(db.String(255), nullable=False)
    
    def __init__(self, application_id,message_id,content):
        self.application_id = application_id
        self.message_id=message_id
        self.content=content
        self.participants=[]
        session_id=""
    
    def validation(self):
        if not isinstance(self.application_id, int):
            return {'message':"invalid application_id" }, 400
        if self.message_id=="" or not self.message_id:
            return {'message':"no message_id provided"}, 400
        if self.content=="" or not self.content:
            return {'message':"no content provided"}, 400
        return None
    
    def add_participant(self,participant):
        self.participants.append(participant)
    def add_session(self,session):
        self.session_id=session
        return self

