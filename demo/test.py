from operator import methodcaller
from flask import Flask,render_template,request,redirect
import os
import pyodbc

host = "192.168.1.15"
app = Flask("__main__")
db = pyodbc.connect("DRIVER={MySQL ODBC 8.0 ANSI Driver}; SERVER=localhost"+"; PORT=3306;DATABASE=quanlyhatang"+"; UID=root"+";PASSWORD="+";OPTION = 3;")
now = []
@app.route('/404')
def err():
    return render_template('404.html')
@app.route('/logout')
def logout():
    return redirect('/')
    return render_template('login.html')
@app.route('/logout/<name>')
def logout_name(name=None):
    if not name or name not in now:
        return 'CHƯA LOGIN'
    else:
        for i in now:
            if i == name:
                del i 
                break
        print(now)
        return render_template('login.html')
@app.route('/',methods = ['POST','GET'])
def demo():
    if request.method == 'GET':
        print("GET LOGIN")
        return render_template('login.html')
    elif request.method == 'POST':
        print("POST LOGIN")
        curs = db.cursor()      
        usr = request.form['username']
        pwd = request.form['password']
        query_str = 'SELECT * FROM `account`;'
        list_acc = curs.execute(query_str)
        # [tk,mk,ban,ngaytao]
        for i in list_acc:
            if usr == i[0]:
                if pwd == i[1]:
                    if int(i[2])==0:
                        now.append(usr)
                        return redirect('/home/'+usr)
        return render_template('404.html')
    else:
        return render_template('404.html')
@app.route('/home/<name>')
def home(name=None):
    if not name or name not in now:
        return 'CHƯA LOGIN'
    return render_template('home.html')
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        print("GET LOGIN")
        return render_template('login.html')
    elif request.method == 'POST':
        print("POST LOGIN")
        print(now)
        curs = db.cursor()      
        usr = request.form['username']
        pwd = request.form['password']
        query_str = 'SELECT * FROM `account`;'
        list_acc = curs.execute(query_str)
        # [tk,mk,ban,ngaytao]
        for i in list_acc:
            if usr == i[0]:
                if pwd == i[1]:
                    if int(i[2])==0:
                        now.append(usr)
                        return redirect('/home/'+usr)

        return render_template('404.html')
    else:
        return render_template('404.html')
if __name__ == "__main__":

    app.run(host=host,port=9999,debug=False)
    