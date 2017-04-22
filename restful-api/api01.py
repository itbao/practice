#!/bin/env python
#coding=utf-8

from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response

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

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201



@app.route('/')
def index():
    return "Hello, World!"
    #Content-Type: text/html; charset=utf-8

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    #Content-Type: application/json

#根据参数返回
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

#改善我们的 404 错误处理程序
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

