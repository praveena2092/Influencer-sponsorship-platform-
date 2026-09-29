import os
from flask import Flask
from application.config import LocalDevelopmentConfig
from application.database import db

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv("ENV", "development") == "production":
        raise Exception("Currently no production config is setup")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
         
     
     
    
    db.init_app(app)
    
    with app.app_context():
        # Importing here to avoid circular imports
        import application.admin_controller 
        import application.rest 
        import application.influencer_controller 
        import application.sponsor_controller
        db.create_all()
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')


