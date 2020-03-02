from flask import Flask,render_template,request,redirect
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index_origin.html")


@app.route('/underbuild')
def underbuild():
	return redirect("https://enjoygame.taobao.com/")



@app.route('/e_store')
def e_store():
    return render_template("e_store.html")





@app.route('/about')
def about():
	return render_template("about.html")


if __name__ == '__main__':
	app.run("127.0.0.1",port=10071,debug=True)