# -*- coding: utf-8 -*-
from flask import Flask, jsonify,render_template
import psutil, time,json

app = Flask(__name__)#实例化app对象

@app.route('/index',methods=['GET', 'POST'])
def index():
    return render_template("index.html")



# 下面的内容是获取服务器的设备信息，然后返回给页面
@app.route('/test_post/aa', methods=['GET','POST'])#路由
def test_post():
    memKeys = ["total", "available", "percent", "used", "free"]#查看内存信息
    memVaules = psutil.virtual_memory()
    memInfo = dict(zip(memKeys, memVaules))
    memInfo = {k: str(v / pow(1024.0, 3)) + 'GB' for k,v in memInfo.items() if k != 'percent'}
    memInfo['percent'] = psutil.virtual_memory().percent
    return "successCallback"+"("+json.dumps(memInfo)+")"#将结果以json形式返回，通过jsonp与前台交互

if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = 10071,debug = True)