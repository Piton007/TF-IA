from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask import Response
import json
from user_services import UserService
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
api = Api(app)


usuarioActual=""

class Stadistics(Resource):
    def get(self):
        return Response(json.dumps(usuarioActual.getStadistics()),status=202,mimetype='application/json')

class Users(Resource):
  
    def post(self):
        global usuarioActual
        name=request.json['UserName']
        limits=request.json['LimitsTweets'] 
        usuarioActual=UserService(name,limits)
        response=""
        if usuarioActual.autenticarUsuario():
            response=Response(json.dumps(usuarioActual.getUserDAO().__dict__), status=202, mimetype='application/json')
            
        else:
            response=Response(json.dumps({"Info":"No existe dicho usuario "+usuarioActual.twitterUser.screen_name}), status=404, mimetype='application/json')
        return response
        
api.add_resource(Users, '/users')
api.add_resource(Stadistics, '/stadistics')

if __name__ == "__main__":
    app.run(debug=True)

