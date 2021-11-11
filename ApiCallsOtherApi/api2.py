from flask import Flask , jsonify , request
import requests
from flask_restful import Resource , Api 

app2 = Flask(__name__)

api = Api(app2)

class Bmi(Resource) : 
    def post(self):
        data = request.get_json()
        weight = float(data['weight'])
        height = float(data['height'])
        bmiuser =  weight / (height)**2
        res2 = requests.post("http://127.0.0.1:5002/score" , json= {'bmi' : bmiuser})
        if(res2.status_code == 200) :
            category = res2.json()['category']
            return jsonify({'category' : category})
        else : 
            print(f'Some error Api2 {res2.status_code}')
            return jsonify({'category' : 'None'})

api.add_resource(Bmi , '/bmi')

if __name__ == "__main__":
    app2.run(port = 5001)