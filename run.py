from flask import Flask
from resources.message import api_bp
from flask_cors import CORS
def create_app(config_filename):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    from models.db import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)