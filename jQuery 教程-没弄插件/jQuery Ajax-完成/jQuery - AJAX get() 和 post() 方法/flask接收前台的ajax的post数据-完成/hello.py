from flask import  Flask,render_template,request,jsonify
from flask_cors import cross_origin
app = Flask(__name__)
import json
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/sendAjax2', methods=['GET','POST'])
@cross_origin()
def sendAjax2():
    # password = request.form.get('password')
    # username = request.args.get('username')
 
    data = json.loads(request.form.get('data'))
    username = data['username']
    password = data['password']
    print (username)
    print (password)

    return jsonify({'tasks': "来自flask的信息"})
    # 这里是返回给index.html


@app.route('/register_success', methods=['GET','POST'])
@cross_origin()
def final():
    return "您已经登录/注册成功!"

    
if __name__ == '__main__':
    app.run("127.0.0.1",port=10071,debug=True)