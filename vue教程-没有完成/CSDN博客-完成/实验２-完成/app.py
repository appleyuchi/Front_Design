from flask import Flask, jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


response_data=[
{
	"id": 1,
	"name": "奥迪",
	"ctime": "2017-02-07T10:32:07.000Z"
},
{	"id": 2,
	"name": "宝马",
	"ctime": "2017-02-07T10:32:17.000Z"
},
{
	"emulateJSON":"true",
	"name": "奔驰",
	"time": "2019-01-13T08:55:45.921Z",
	"id": 3
}]


#----------------------------------------------------------------------------------------------------
@app.route('/message', methods=['GET'])
def vue_get():
    print("request.args=",request.args)

    return jsonify(response_data)
    #（jsonify返回一个json格式的数据）


@app.route('/post_message', methods=['POST'])
def vue_post():
    print("request.form=",request.form)

    return jsonify(response_data)
    #（jsonify返回一个json格式的数据）




if __name__ == '__main__':
    app.run(host='127.0.0.1',port=10071,debug=True)

