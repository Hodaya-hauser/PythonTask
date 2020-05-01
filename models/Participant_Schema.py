from models.db import db,ma
from marshmallow import Schema, fields  
class Participant_Schema(ma.Schema):
    participant_name = fields.String(required=True)