from flask import Flask
from flask_restful import Resource, Api
from resources.whoishome import WhoIsHome
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')



class StaticWhoIsHome(Resource):
    def get(self):
        return [{'name': 'Horacio'}, {'name': 'Johannes'}]

api.add_resource(StaticWhoIsHome, '/whoishomestatic')




api.add_resource(WhoIsHome, '/whoishome')

if __name__ == '__main__':
    app.run(debug=True)