from flask import  Flask,render_template,request
from flask_cors import cross_origin
import pymysql
app = Flask(__name__)

@app.route("/load_test",methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template("index.html")


# 提交修改   因为pymysql 模块默认是启用事务的  你的sql语句 如果不提交 相当于没有执行
# conn.commit()
@app.route("/query_database",methods=['GET'])
def index2():
    q=request.args.get("q") 
    data=query(q)#这里返回的是元组形式

    t2='<br>'.join(data)
    return t2


#----------------------------------------------下面是非交互函数-----------------------------------------------------------------------------------
def query(q):
    # 连接mysql字符串
    conn = pymysql.connect(host="localhost",user= "appleyuchi",password= "appleyuchi", database="ajax_data",port=3306)
    # 新建游标
    cursor = conn.cursor()
    # 执行sql语句
    cursor.execute("select  *  from company_info where CustomerID=(%s)",q)
    # data = cursor.fetchall()
    data=cursor.fetchone()
    return data

#---------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # 测试数据库链接是否ok
    # q="APPLE"
    # data=query(q)
    # print("data=",data)

    app.run("127.0.0.1",port=10071,debug=True)