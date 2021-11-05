from flask import Flask, request
from flask_restful import Resource, Api
import json
import datetime

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return "Martijn is baas van het internet"

class DataStream(Resource):
    def get(self):
        return "Input data using post, data should be under the header \"data\""

    def put(self):
        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        data = request.form['data']
        with open(f"../Data/{timestamp}.csv", "w") as f:
            f.write(data)
        return "Succesfully added data"


api.add_resource(HelloWorld, '/')
api.add_resource(DataStream, '/data')

if __name__ == '__main__':
    app.run(debug=True)
