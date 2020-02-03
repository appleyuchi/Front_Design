#coding:utf8
from flask import Flask,jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import cross_origin
 

app = Flask(__name__)

 

jobs = [
    {
        'id': 1,
        'post': u'运维工程师',
        'level':'professor'
    },
    {
        'id': 2,
        'post': '产品经理',
        'level':'primary'
    }
]

 

@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
@cross_origin()
def get_tasks():
    print(request.args)

    print("进入第１个函数")
    return jsonify({'jobs':jobs})

 

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@cross_origin()
def get_task(task_id):
    print("进入第２个函数")
    task = filter(lambda t: t['id'] == task_id, jobs)
    #print (list(task))
    task = list(task)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task})

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=10071)
