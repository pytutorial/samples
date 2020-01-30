from flask import Blueprint, render_template

html_pages = Blueprint('html_pages', __name__)

@html_pages.route('/')
def index():
    return render_template('index.html', name="test")

@html_pages.route('/page2')
def page2():
    return render_template('page2.html')

@html_pages.route('/page3')
def page3():
    return render_template('page3.html')