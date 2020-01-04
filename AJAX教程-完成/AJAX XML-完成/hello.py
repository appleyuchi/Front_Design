from flask import  Flask,render_template,request
from flask_cors import cross_origin
import pymysql
app = Flask(__name__)

@app.route("/load_test",methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template("index.html")


if __name__ == '__main__':

    app.run("127.0.0.1",port=10071,debug=True)