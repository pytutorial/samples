from app import app, db
from html_pages import html_pages
from service import service

app.register_blueprint(html_pages)
app.register_blueprint(service)
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    
