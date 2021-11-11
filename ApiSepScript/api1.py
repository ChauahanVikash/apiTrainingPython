from flask import Flask , jsonify , request
from flask_restful import Resource , Api

import json 

app = Flask(__name__)

api1 = Api(app)


@app.route("/", methods = ['POST'])
def home_page( ):
    data = request.get_json()
    age  = int(data['age'])
    number = int(data['number'])
    return jsonify({"ans1" : age + number})

if __name__ == "__main__" :
    app.run(port=5001)