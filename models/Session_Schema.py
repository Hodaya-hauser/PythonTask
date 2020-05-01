from models.db import ma
from marshmallow import Schema, fields
class Session_Schema(ma.Schema):
    session_id = fields.String(required=True)
    messages = fields.List(fields.Nested("Message_Schema"), exclude=("message_id",),required=True)