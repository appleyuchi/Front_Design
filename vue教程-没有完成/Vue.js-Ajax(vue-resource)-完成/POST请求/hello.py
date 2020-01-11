from flask import Flask,render_template,jsonify,request
import json
from  flask_cors import cross_origin
app = Flask(__name__)
#----------------------------------------------------
@app.route("/index",methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template("index.html")


@app.route("/post_method",methods=['GET', 'POST'])
def post_method():
    print("request.form=",request.form)
    name = request.form.get('name')
    url  = request.form.get('url')
    return "website name: "+name+" URL name: "+url

if __name__ == '__main__':
	app.run("127.0.0.1",port=10071,debug=True)
