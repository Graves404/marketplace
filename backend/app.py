import os
from flask import Flask, jsonify, Response
from flask_cors import CORS
from src.queries.orm import select_users, insert_item,insert_user, get_user_items
import json

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*' : {'origins':'*'}})

@app.route('/user', methods=['GET'])
def get_users():
    users = select_users()
    return Response(json.dumps(users), mimetype="application/json")

if __name__ == '__main__':
    app.run

