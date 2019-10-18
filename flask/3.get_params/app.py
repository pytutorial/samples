from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')    # http://localhost:5000/hello?name=Nguyễn+Văn+An
def hello():
    name = request.args.get("name", "")
    return "Hello " + name
    
app.run(debug=True)    