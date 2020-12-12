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
