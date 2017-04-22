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
        'done': False
    },
    {
        'id': 2,
        'title': u'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ',
        'done': False
    }
]

@app.route('/')
def index():
    return """
   curl -i  localhost:5000/api/v1.0/tasks

   curl -i -H "Content-Type: application/json" -X POST \
-d '{"title":"Newtitle"}' localhost:5000/api/v1.0/tasks
"""
@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)

    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title', "Default update title")
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({'task': task[0]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
