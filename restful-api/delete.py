#!/bin/env python
#coding=utf-8

from flask import Flask
from flask import jsonify
from flask import abort

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
    curl -i http://localhost:5000/api/v1.0/tasks
    curl -i -X DELETE http://localhost:5000/api/v1.0/tasks/2
"""

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    #Content-Type: application/json



@app.route('/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
