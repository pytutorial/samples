from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
from urllib.parse import quote

Base = declarative_base()

password = quote('abc@123')
engine = create_engine(f'mysql://test:{password}@34.122.175.106/py2103')

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    code = Column(String(20))
    name = Column(String(100))
    price = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)


