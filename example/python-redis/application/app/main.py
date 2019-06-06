import socket
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/ping')
class HelloWorld(Resource):
    def get(self):
        return {'pong': socket.gethostname()}

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
