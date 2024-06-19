from flask import Flask,redirect
app = Flask('app')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/google')
def google():
    return redirect("http://www.google.com")

@app.route('/eastmoney')
def eastmoney():
    return redirect("http://stock.jrj.com.cn/share,000830,gdhs.shtml")

app.run(host='0.0.0.0', port=8080)
