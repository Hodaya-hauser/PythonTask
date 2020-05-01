from models.db import db
class Session(db.Model):
    __tablename__ = 'Session'
    session_id = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    messages = db.relationship("Message", backref='session', lazy='dynamic')

    def __init__(self, session_id):
        self.session_id = session_id
        self.messages=[]

    def add_message(self,message):
        self.messages.append(message.add_session(self.session_id))
        
        
    def validation(self):
        if self.session_id=="":
            return {'message': 'invalid session_id'}, 400
        return None