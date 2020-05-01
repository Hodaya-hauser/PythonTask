from models.db import ma
from marshmallow import Schema, fields
from models.Participant_Schema import Participant_Schema
from models.Session_Schema import Session_Schema
class Message_Schema(ma.Schema):
    application_id = fields.Int(required=True)
    session_id = fields.String(required=True)
    message_id=fields.String(required=True)
    participants=fields.List(fields.Nested("Participant_Schema",required=True))
    content=fields.String(required=True)

    def add(self,participant):
        self.participants.append(participant)