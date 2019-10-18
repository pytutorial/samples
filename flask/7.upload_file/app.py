import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/upload', methods=['POST'])
def uploadImage():
    file = request.files.get('image')
    if file != None and file.filename != '':
        file.save(os.path.join('static', file.filename))
        return redirect('/static/' + file.filename)
    else:
        return "Cannot upload file"
    
app.run(debug=True)    