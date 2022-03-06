import json
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []


@app.route("/", methods=['GET'])
def get_users():
    return jsonify(users)


@app.route("/", methods=['POST'])
def post_users():
    body = json.loads(request.data)
    new_user= {
        "name": body['name'],
        "lastname": body['lastname'],
        "email": body['email']
    }
    users.append(new_user)
    return jsonify(new_user)


if __name__ == '__main__':
    app.run(debug=True)
