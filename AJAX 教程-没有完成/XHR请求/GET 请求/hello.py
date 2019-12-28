from flask import  Flask,render_template,request
from flask_cors import cross_origin
app = Flask(__name__)
 
 
@app.route("/load_test",methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template("index.html")
 
@app.route('/test',methods=['GET', 'POST'])
def ajax_data():
    # 获取get参数
    fname=request.args.get("fname")
    lname=request.args.get("lname")
    # 获取post参数
    # fname=request.form['fname']
    # lname=request.form['lname']


    # 注意Flask获取get参数和获取post参数的方式是不一样的

    print("fname=",fname)
    print("lname=",lname)
    return "你好，"+fname+" "+ lname+"，今天过得怎么样？"
    # 这里的return是返回给xhr请求接收


if __name__ == '__main__':
    app.run("127.0.0.1",port=10071,debug=True)