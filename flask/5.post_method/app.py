from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        fullname = request.form.get('fullname', '')
        address = request.form.get('address', '')
        return f'Họ tên : {fullname}, địa chỉ : {address}'
    
app.run(debug=True)    