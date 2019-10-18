from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/static/sample.jpg')
    
app.run(debug=True)    