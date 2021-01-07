from sqlalchemy import Column, Integer, String, Text
from models.database import Base


class YarukotoList(Base):
    __tablename__ = 'yarukotolists'
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    body = Column(Text)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Title %r>' % (self.title)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)
