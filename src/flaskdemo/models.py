from flask import Flask
from sqlalchemy import Column, Integer, String
from database import Base


class Contact(Base):
  __tablename__ = 'contact'
  id     = Column(Integer, primary_key=True)
  name   = Column(String)
  number = Column(String)

  def __init__(self, name, number):
    self.name   = date
    self.number = value

  def __repr__(self):
    s = "<Contact '{}' with phone number '{}'>"
    return s.format(self.name, self.number)
