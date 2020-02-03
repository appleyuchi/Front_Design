from flask import Flask,render_template,jsonify,request
import json
from  flask_cors import cross_origin
app = Flask(__name__)



json_data={"data":{"name":"菜鸟教程","url": "https://www.runoob.com" }, "status": 200, "statusText": "OK", "headers": { "ali-swift-global-savetime": "1578574596", "content-encoding": "gzip", "content-length": "93", "content-type": "text/html; charset=UTF-8", "date": "Thu, 09 Jan 2020 12:56:36 GMT", "eagleid": "3d9bddcc15785745962345938e", "server": "Tengine", "timing-allow-origin": "*", "vary": "Accept-Encoding", "via": "cache47.l2cn1807[46,200-0,M], cache47.l2cn1807[48,0], cache4.cn58[83,200-0,M], cache4.cn58[93,0]", "x-cache": "MISS TCP_MISS dirn:-2:-2", "x-firefox-spdy": "h2", "x-m-log": "QNM:jjh1874;SRCPROXY:jjh1497;SRC:14;SRCPROXY:14;QNM3:15", "x-m-reqid": "0w8AAGgC-U87OegV", "x-qnm-cache": "RawProxy", "x-swift-cachetime": "0", "x-swift-savetime": "Thu, 09 Jan 2020 12:56:36 GMT" }, "config": { "transformRequest": {}, "transformResponse": {}, "timeout": 0, "xsrfCookieName": "XSRF-TOKEN", "xsrfHeaderName": "X-XSRF-TOKEN", "maxContentLength": -1, "headers": { "Accept": "application/json, text/plain, */*" }, "method": "post", "url": "https://www.runoob.com/try/ajax/demo_axios_post.php" }, "request": {} } 


# json_data={"name":"yuchi","url":"www.baidu.com"}
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
    return jsonify(json_data)
    # return "website name: "+name+" URL name: "+url
    # return "axios hello world"

if __name__ == '__main__':
	app.run("127.0.0.1",port=10071,debug=True)
