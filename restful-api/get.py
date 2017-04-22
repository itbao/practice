#!/bin/env python
#coding=utf-8

from flask import Flask
from flask import jsonify
from flask import abort
#from flask import make_response

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


from flask import request



@app.route('/')
def index():
    return """
    curl -i http://localhost:5000/api/v1.0/tasks
    curl -i http://localhost:5000/api/v1.0/tasks/1
    curl -i http://localhost:5000/api/v1.0/tasks/2
"""
    #Content-Type: text/html; charset=utf-8

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    #Content-Type: application/json

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

