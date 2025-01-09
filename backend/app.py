import os
from flask import Flask, jsonify, json
from flask_cors import CORS
from src.queries.orm import select_users, insert_item,insert_user, select_user_by_city 

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*' : {'origins':'*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    insert_item("Honda")
    select_user_by_city("Donghu")
    return jsonify('TEST')

if __name__ == '__main__':
    app.run

