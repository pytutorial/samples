from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

jinja_options = app.jinja_options.copy()
jinja_options.update({
    "variable_start_string" : '{%=',
    "variable_end_string" :'%}'
})
app.jinja_options = jinja_options

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)