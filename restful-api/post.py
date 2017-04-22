#!/bin/env python
#coding=utf-8

from flask import Flask
from flask import jsonify
from flask import abort
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'description': u'This is description',
        'done': False
    },
    {
        'id': 2,
        'title': u'This is description',
        'done': False
    }
]

@app.route('/')
def index():
    return """
curl -i http://localhost:5000/api/v1.0/tasks

curl -i -H "Content-Type: application/json" \
-X POST -d '{"title":"Read a abook","description":"SSSS"}' \
http://localhost:5000/api/v1.0/tasks/2
"""

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "Default description"),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
