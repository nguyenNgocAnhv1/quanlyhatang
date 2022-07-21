from flask import Flask,render_template
import os

app = Flask("__main__")

@app.route('/')
def demo():
    return render_template('index.html')
if __name__ == "__main__":
    #os.system("start http://127.0.0.1:9999")
    app.run("192.168.1.15",port=9999,debug=True)
    