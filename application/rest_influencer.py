from flask_restful import Resource,Api
from flask import current_app as app
from .database import db
api=Api(app)

class SecondResource(Resource):
    def get(self):
        return "Successfully Signed Up"
    def post(self):
        return "this is post request"
    def put(self):
        return "Updated Successfully"
    def delete(self):
        
        return "Deleted Successfully"
    
api.add_resource(SecondResource,"/influencer_api")