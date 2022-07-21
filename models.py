from sqlalchemy import Column, Integer, String

from database import Base

class ItemModel(Base):
    __tablename__ = "items"
    __table_args__ = {'schema': 'cc'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sex = Column(String, index=True)
    color = Column(String)

