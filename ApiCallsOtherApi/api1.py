from flask import Flask,jsonify, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)

api = Api(app)

class conv(Resource):
    def post(self):
        data = request.get_json()
        name = str(data['name'])
        weight = float(data['weight'])/1000
        height = float(data['height'])/3.28 
        res1 = requests.post("http://127.0.0.1:5001/bmi" , json= {'weight' : weight ,'height' : height})
        if res1.status_code == 200 :
            
            category = res1.json()['category']
            return jsonify({'message' : f'Hi {name}! You are {category}.'})
        else : 
            print(f"Some error api1 {res1.status_code}")


api.add_resource(conv, '/conversion')

if __name__=='__main__':

    app.run(debug = True,host='127.0.0.1',port=5000)