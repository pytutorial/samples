from flask import Flask

app = Flask(__name__)

@app.route('/')  # http://localhost:5000
def index():
    return "Hello"
    
app.run(debug=True)    