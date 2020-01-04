from flask import  Flask,render_template,request
from flask_cors import cross_origin
app = Flask(__name__)
 
 
@app.route("/load_test",methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template("index2.html")
 
@app.route('/test',methods=['GET', 'POST'])
def ajax_data():
    fname=request.form['fname']
    lname=request.form['lname']
    print("fname=",fname)
    print("lname=",lname)
    return "你好，"+fname+" "+ lname+"，今天过得怎么样？"


if __name__ == '__main__':
    app.run("127.0.0.1",port=10071,debug=True)