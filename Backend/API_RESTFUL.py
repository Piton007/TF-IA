from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from tweetdata import *


app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {"Hello":name}
    def post(self):
        user_name = request.json['UserName']
        return {'status': 'Registro de usuario correcto'}
        
api.add_resource(Users, '/users')

if __name__ == "__main__":
    app.run(debug=True)

