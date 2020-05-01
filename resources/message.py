
from flask import request, jsonify
from flask_restful import Resource
import json
from models.db import db
from models.Message import Message
from models.Participant import Participant
from models.Session import Session
from app import api_bp
from models.Message_Schema import Message_Schema
from models.Participant_Schema import Participant_Schema
from models.Session_Schema import Session_Schema
from marshmallow import Schema, fields, ValidationError, pre_load
message_schema=Message_Schema()
messages_schema=Message_Schema(many=True)
participant_schema=Participant_Schema()
participants_schema=Participant_Schema(many=True)
participants_schema=Participant_Schema(many=True)
session_schema=Session_Schema()
class MessageResource(Resource):
    
    @api_bp.route("AddMessage" , methods=["POST"])
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        if  not "application_id" in json_data or  not "session_id" in json_data or not "message_id" in json_data  or not "participants" in json_data or not "content" in json_data:
            return {"message":"not provide all params"},400
        application_id = json_data['application_id']
        session_id = json_data['session_id']
        message_id = json_data['message_id']
        participants = json_data['participants']
        content = json_data['content']     
        message=Message(application_id, message_id,content)
        if Message.query.get(message_id):
            return {"message": "Message already exists"}, 400 
        try:
            if not participants:
                return {"message": "no participants provided"}, 400
            for x in participants:
                if Participant.query.get(x) is None:
                    participant=Participant(x)
                    if  participant.validation() is not None:
                        return participant.validation()
                    db.session.add(participant)
                else:
                    participant=Participant.query.get(x)
                message.add_participant(participant)
            if Session.query.get(session_id) is None:
                session = Session(session_id)
                result = session_schema.dump(message)
                if session.validation() is not None:
                    return session.validation()
                if  message.validation() is not None:
                    return message.validation()
                db.session.add(session)
                session.add_message(message)
            else:
                session=Session.query.get(session_id)
                session.add_message(message)
                if  message.validation() is not None:
                    return  message.validation()
            db.session.add(message)
            db.session.commit()
        except Exception as e:
            print("Failed to add message")
            print(e)
            db.session.rollback()
            return {"message":"error"}
        db.session.close()   
        return { "status": "success" }, 201

    @api_bp.route("GetMessage", methods=["GET"])
    def get():
        messages=[]
        input_data=""
        if request.args.get("application_id"):
            input_data=request.args.get("application_id")
            if  input_data.isdigit() == False:
                return {'message': 'invalid application_id'}  , 400  
            messages=db.session.query(Message).filter_by(application_id = input_data).all()
        if request.args.get('session_id'):
            input_data=request.args.get("session_id")
            messages=db.session.query(Message).filter_by(session_id = input_data).all()
        if request.args.get('message_id'):
            input_data=request.args.get("message_id")
            messages=db.session.query(Message).filter_by(message_id = input_data).all()
            if  messages:
                json_output=messages_schema.dump(messages)
                return {"message": json_output}
            else:
                return {'message': 'No message found'}, 200
        elif not input_data:
            return {'message': 'No input data provided'}, 400
        else:
            if  messages:
                json_output=messages_schema.dump(messages)
            else:
                return {'message': 'No message found'}, 200
        return {"messages": json_output}
    @api_bp.route("DeleteMessage", methods=["GET"])
    def delete():
        messages=[]
        input_data=""
        try:
            if request.args.get("application_id"):
                input_data=request.args.get("application_id")
                if input_data.isdigit() == False:
                    return {'message': 'invalid application_id'}, 400
                messages=db.session.query(Message).filter_by(application_id = input_data).all()
            if request.args.get('session_id'):
                input_data=request.args.get("session_id")
                messages=db.session.query(Message).filter_by(session_id = input_data).all()
            if request.args.get('message_id'):
                input_data=request.args.get("message_id")
                messages=db.session.query(Message).filter_by(message_id = input_data).all()
            if not input_data:
                return {'message': 'No input data provided'}, 400
            if not messages:
                 return {'message': 'No message found'} ,404
            else:
                for message in messages:
                    db.session.delete(message)
                    db.session.commit()
        except Exception as e:
            print("Failed to delete message")
            print(e)
            return {"message": "error"} 
        return {"status": "success"}, 200