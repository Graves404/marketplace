import os
from flask import Flask, jsonify, json
from flask_cors import CORS
from src.queries.orm import fetch_all_users

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*' : {'origins':'*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    rows = fetch_all_users()
    return jsonify('TEST')

if __name__ == '__main__':
    app.run

