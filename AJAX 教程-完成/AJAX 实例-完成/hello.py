from flask import  Flask,render_template
app = Flask(__name__)
 
 
@app.route("/load_test",methods=['GET', 'POST'])
def index():
    return render_template("index.html")
 
# @app.route('/ajax_get',methods=['GET', 'POST'])
# def ajax_data():
#     return "这个是来自flask的数据"


if __name__ == '__main__':
    app.run("127.0.0.1",port=10071,debug=True)