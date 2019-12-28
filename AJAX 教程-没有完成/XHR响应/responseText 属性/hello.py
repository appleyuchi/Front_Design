from flask import  Flask,render_template,request
from flask_cors import cross_origin
app = Flask(__name__)
 
 
@app.route("/load_test",methods=['GET', 'POST'])
@cross_origin()
def index():
    print("这里是XHR响应")
    return render_template("index.html")


if __name__ == '__main__':
    app.run("127.0.0.1",port=10071,debug=True)