
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

Base = declarative_base()

password = quote('abc@123')
engine = create_engine(f'mysql://test:{password}@34.122.175.106/py2103?charset=utf8')
Session = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100))

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category")
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(100))
    price = Column(Integer)

def createCategory(code, name):
    category = Category(code=code, name=name)
    session = Session()
    session.add(category)
    session.commit()

def getCategoryById(id):
    session = Session()
    return session.query(Category).filter(Category.id == id).first()

def deleteCategory(id):    
    session = Session()
    session.query(Category).filter(Category.id == id).delete()
    session.commit()

def updateCategory(id, code, name):
    session = Session()
    category = session.query(Category).filter(Category.id == id).first()
    if category:
        category.code = code
        category.name = name
        session.commit()

def createProduct(code, name, price, category_code):
    session = Session()
    category = session.query(Category).filter(Category.code==category_code).first()
    product = Product(code=code, name=name, price=price, category=category)
    session.add(product)
    session.commit()

def searchProduct(category_code, keyword):
    session = Session() 
    return session.query(Product).join(Category).filter(
                Category.code == category_code,
                Product.name.like('%'+keyword+'%'))
    # Compare: Product.price > , <, >=, <=, != price
    # or: _or(Product.code.like('%'+keyword+'%'), Product.name.like('%'+keyword+'%')) # from sqlalchemy import or_
    # in: Product.id.in_([1,2,3])

if __name__ == '__main__':
    Base.metadata.create_all(engine)
