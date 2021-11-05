from flask import Flask, request
from flask_restful import Resource, Api
import json
import datetime
import pickle as pck

app = Flask(__name__)
api = Api(app)

model_path = 'model.pickle'

class HelloWorld(Resource):
    def get(self):
        return "Martijn is baas van de apen"

class DataStream(Resource):
    def get(self):
        return "Input data using post, data should be under the header \"data\""

    def put(self):
        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        data = request.form['data']

        with open(f"Data/{timestamp}.csv", "w") as f:
            f.write(data)
        return "Succesfully added data"

class Prediction(Resource):
    def get(self):
        return "Geef data"

    def check_data(self,data):
        d = json.loads(data)
        if d.keys() != ['IR Voltage', 'Temperature','Time','Date']:
            return False
        return True

    def post(self):
        data = request.form['data']
        if self.check_data(data):
            model = pck.load(model_path)
            if isinstance(data, list):
                return model.predict(data)
            return model.predict([data])
        else:
            print("Geef betere data noob")


api.add_resource(HelloWorld, '/')
api.add_resource(DataStream, '/data')

if __name__ == '__main__':
    app.run(debug=True)
