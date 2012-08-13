from flask import Flask
from sqlalchemy import Column, Integer, String
from database import Base


class Contact(Base):
  __tablename__ = 'contact'
  name   = Column(String, primary_key=True)
  number = Column(String)

  def __init__(self, name, number):
    self.name   = name
    self.number = number

  def __repr__(self):
    s = "<Contact '{}' with phone number '{}'>"
    return s.format(self.name, self.number)
