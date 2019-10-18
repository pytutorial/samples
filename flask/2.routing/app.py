from flask import Flask

app = Flask(__name__)

@app.route('/')                     # http://localhost:5000
def index():
    return "Home page"

@app.route('/hello')                # http://localhost:5000/hello
def hello():
    return "Hello"

@app.route('/hello/<name>')         # http://localhost:5000/hello/Nguyen Van An
def hello2(name):
    return "Hello " + name
    
app.run(debug=True)    