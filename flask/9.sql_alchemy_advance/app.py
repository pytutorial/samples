from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

BookCategs = db.Table('book_categs',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='author_ref', lazy=True)
  
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50))  
    books = db.relationship("Book", secondary=BookCategs, lazy="subquery",
                    backref=db.backref("category_ref", lazy=True))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50)) 
    authorId = db.Column('author_id', db.Integer, db.ForeignKey('author.id'), nullable=False)
    categories = db.relationship("Category", secondary=BookCategs, lazy="subquery",
                    backref=db.backref("book_ref", lazy=True))
    
def createDbTest():
    author = Author()
    author.code = 'AUTH_0001'
    author.name = 'Author 1'
    db.session.add(author)
    
    categ1 = Category()
    categ1.code = 'C1'
    categ1.name = 'Category 1'
    db.session.add(categ1)
        
    categ2 = Category()
    categ2.code = 'C2'
    categ2.name = 'Category 2'
    db.session.add(categ2)

    db.session.commit()
    
    book = Book()
    book.code = 'B1'
    book.name = 'Book 1'
    book.authorId = author.id
    book.categories = [categ1, categ2]
    db.session.add(book)    
    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    if Book.query.count() == 0:
        createDbTest()
        
    book = Book.query.get(1)
    print(book.code, book.name, book.authorId, book.categories)
    
    categ = Category.query.get(1)
    print(categ.code, categ.name, categ.books)
    
    #app.run(debug=True)