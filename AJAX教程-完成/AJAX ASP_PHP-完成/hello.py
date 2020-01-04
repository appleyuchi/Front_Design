from flask import  Flask,render_template,request
from flask_cors import cross_origin
app = Flask(__name__)
 
name_list=["Anna","Brittany","Cinderella","Diana","Eva","Fiona","Gunda","Hege","Inga","Johanna","Kitty","Linda","Nina","Ophelia","Petunia","Amanda","Raquel","Cindy","Doris","Eve","Evita","Sunniva","Tove","Unni","Violet","Liza","Elizabeth","Ellen","Wenche","Vicky"]
@app.route("/load_test",methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template("index.html")



@app.route("/test",methods=['GET', 'POST'])
def index2():
    q=request.args.get("q") 
    if q in name_list:
        return q
    else:
        return "no suggestion"


if __name__ == '__main__':
    app.run("127.0.0.1",port=10071,debug=True)