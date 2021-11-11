from flask import Flask , jsonify , request
from flask_restful import Resource , Api

app = Flask(__name__)

api1 = Api(app)


@app.route("/", methods = ['POST'])
def home_page():
    data = request.get_json()
    return jsonify({'ans2' : int(data['number'])//2})

if __name__ == "__main__" :
    app.run(port=5002)