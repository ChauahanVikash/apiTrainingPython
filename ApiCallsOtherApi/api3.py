from flask import Flask , jsonify , request
from flask_restful import Resource , Api 

app3 = Flask(__name__)

api = Api(app3)

class Score(Resource) :
    def post(self):
        data = request.get_json()
        bmi = float(data['bmi'])
        message = ""
        if(bmi < 18.5):
            message = "Underweight"
        elif(bmi  < 24.9):
            message = 'Healthy'
        elif(bmi < 29.9):
            message = 'Overweight'
        else : 
            message = 'Obese'
        return jsonify({"category" : message})

api.add_resource(Score,'/score')
if __name__ == '__main__':
    app3.run(port = 5002)


