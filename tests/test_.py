
from models.Message import Message
from models.Participant import Participant
from models.Session import Session
import json
import pytest
from run  import create_app
def test_AddMessage1(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"1",
        "message_id":"1",
        "participants":["aaa","bbb"],
        "content":"message1"
    }
    url = '/AddMessage'

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["status"]=="success"
    assert response.status_code == 201

def test_AddMessage2(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"2",
        "message_id":"2",
        "participants":["eee","fff"],
        "content":"message1"
    }
    url = '/AddMessage'

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["status"]=="success"
    assert response.status_code == 201

def test_AddMessage3(client):

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"2",
        "message_id":"3",
        "participants":["aaa","bbb"],
        "content":"message1"
    }
    url = '/AddMessage'

    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["status"]=="success"
    assert response.status_code == 201

def test_AddMessage_not_provided(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {}
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="No input data provided"
    assert response.status_code == 400

def test_AddMessage_exist(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"1",
        "message_id":"1",
        "participants":["ccc","ddd"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="Message already exists"
    assert response.status_code == 400

def test_AddMessage_no_participants(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"1",
        "message_id":"invalid_message000",
        "participants":[],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="no participants provided"
    assert response.status_code == 400


   
def test_AddMessage_not_provide_application_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "session_id":"10",
        "message_id":"",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="not provide all params"
    assert response.status_code == 400

def test_AddMessage_not_provide_session_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "message_id":"",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="not provide all params"
    assert response.status_code == 400


def test_AddMessage_not_provide_message_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"10",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="not provide all params"
    assert response.status_code == 400


def test_AddMessage_not_provide_participants(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"10",
        "message_id":"",
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="not provide all params"
    assert response.status_code == 400

def test_AddMessage_not_provide_content(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"10",
        "message_id":"",
        "participants":["aaa"],
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="not provide all params"
    assert response.status_code == 400



def test_AddMessage_invalid_application_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":"aaa",
        "session_id":"10",
        "message_id":"invalid_message000",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="invalid application_id"
    assert response.status_code == 400

def test_AddMessage_no_session(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"",
        "message_id":"invalid_message",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="invalid session_id"
    assert response.status_code == 400
 
def test_AddMessage_no_message_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"10",
        "message_id":"",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="no message_id provided"
    assert response.status_code == 400

def test_AddMessage_no_participant(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"1",
        "message_id":"invalid_message",
        "participants":["aaa",""],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="no participant provided"
    assert response.status_code == 400

def test_AddMessage_no_content(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"10",
        "message_id":"invalid_message",
        "participants":["aaa"],
        "content":""
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="no content provided"
    assert response.status_code == 400

def test_AddMessage_session_exist_invalid_application_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":"aaa",
        "session_id":"1",
        "message_id":"invalid_message111",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="invalid application_id"
    assert response.status_code == 400

def test_AddMessage_session_exist_no_message_id(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"1",
        "message_id":"",
        "participants":["aaa"],
        "content":"message1"
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="no message_id provided"
    assert response.status_code == 400

def test_AddMessage_session_exist_no_content(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "application_id":1,
        "session_id":"1",
        "message_id":"invalid_message",
        "participants":["aaa"],
        "content":""
    }
    url = '/AddMessage'
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.json["message"]=="no content provided"
    assert response.status_code == 400

def test_GetMessage_invalid_application_id(client):
    response = client.get('/GetMessage?application_id=aaa')
    assert response.status_code == 400
    assert response.json["message"]=="invalid application_id"

def test_GetMessage_not_found_application_id(client):
    response = client.get('/GetMessage?application_id=111')
    assert response.status_code == 200
    assert response.json["message"]=="No message found"

def test_GetMessage_not_found_session_id(client):
    response = client.get('/GetMessage?session_id=000')
    assert response.status_code == 200
    assert response.json["message"]=="No message found"

def test_GetMessage_not_found_message_id(client):
    response = client.get('/GetMessage?message_id=000')
    assert response.status_code == 200
    assert response.json["message"]=="No message found"

def test_GetMessage_not_provided_application_id(client):
    response = client.get('/GetMessage?application_id=')
    assert response.status_code == 400
    assert response.json["message"]=="No input data provided"

def test_GetMessage_not_provided_session_id(client):
    response = client.get('/GetMessage?session_id=')
    assert response.status_code == 400
    assert response.json["message"]=="No input data provided"

def test_GetMessage_not_provided_message_id(client):
    response = client.get('/GetMessage?message_id=')
    assert response.status_code == 400
    assert response.json["message"]=="No input data provided"

def test_GetMessage_application_id(client):
    response = client.get('/GetMessage?application_id=1')
    assert response.status_code == 200
    assert response.json["messages"]==[
    {
      "application_id": 1,
      "content": "message1",
      "message_id": "1",
      "participants": [
        {
          "participant_name": "aaa"
        },
        {
          "participant_name": "bbb"
        }
      ],
      "session_id": "1"
    },
    {
      "application_id": 1,
      "content": "message1",
      "message_id": "2",
      "participants": [
        {
          "participant_name": "eee"
        },
        {
          "participant_name": "fff"
        }
      ],
      "session_id": "2"
    },
    {
      "application_id": 1,
      "content": "message1",
      "message_id": "3",
      "participants": [
        {
          "participant_name": "aaa"
        },
        {
          "participant_name": "bbb"
        }
      ],
      "session_id": "2"
    }
  ]
   


def test_GetMessage_session_id(client):
    response = client.get('/GetMessage?session_id=1')
    assert response.status_code == 200
    assert response.json["messages"]==[
    
    {
      "application_id": 1,
      "content": "message1",
      "message_id": "1",
      "participants": [
        {
          "participant_name": "aaa"
        },
        {
          "participant_name": "bbb"
        }
      ],
      "session_id": "1"
    }
  ]

def test_GetMessage_message_id(client):
    response = client.get('/GetMessage?message_id=2')
    assert response.status_code == 200
    assert response.json["message"]==[
    {
      "application_id": 1,
      "content": "message1",
      "message_id": "2",
      "participants": [
        {
          "participant_name": "eee"
        },
        {
          "participant_name": "fff"
        }
      ],
      "session_id": "2"
    }
  ]

def test_DeleteMessage_invalid_application_id(client):
    response = client.get('/DeleteMessage?application_id=aaa')
    assert response.status_code == 400
    assert response.json["message"]=="invalid application_id"

def test_DeleteMessage_not_found_application_id(client):
    response = client.get('/DeleteMessage?application_id=10000')
    assert response.status_code == 404
    assert response.json["message"]=="No message found"

def test_DeleteMessage_not_found_session_id(client):
    response = client.get('/DeleteMessage?session_id=000')
    assert response.status_code == 404
    assert response.json["message"]=="No message found"

def test_DeleteMessage_not_found_message_id(client):
    response = client.get('/DeleteMessage?message_id=000')
    assert response.status_code == 404
    assert response.json["message"]=="No message found"

def test_DeleteMessage_not_provided_application_id(client):
    response = client.get('/DeleteMessage?application_id=')
    assert response.status_code == 400
    assert response.json["message"]=="No input data provided"

def test_DeleteMessage_not_provided_session_id(client):
    response = client.get('/DeleteMessage?session_id=')
    assert response.status_code == 400
    assert response.json["message"]=="No input data provided"

def test_DeleteMessage_not_provided_message_id(client):
    response = client.get('/DeleteMessage?message_id=')
    assert response.status_code == 400
    assert response.json["message"]=="No input data provided"

def test_DeleteMessage_session_id(client):
    response = client.get('/DeleteMessage?session_id=1')
    assert response.status_code == 200
    assert response.json["status"]=="success"

def test_DeleteMessage_message_id(client):
    response = client.get('/DeleteMessage?message_id=2')
    assert response.status_code == 200
    assert response.json["status"]=="success"

def test_DeleteMessage_application_id(client):
    response = client.get('/DeleteMessage?application_id=1')
    assert response.status_code == 200
    assert response.json["status"]=="success"

@pytest.fixture
def client():
  client = create_app("config").test_client()
  return client


