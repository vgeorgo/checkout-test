import os
import json
import datetime
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def setup_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data', 'data.sqlite')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.app = app
  db.init_app(app)

class Category(db.Model, SerializerMixin):
  __tablename__ = 'categories'
  
  serialize_only = ('id', 'name', 'image_id')
  serialize_rules = ()
  
  ## ATTRIBUTES
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  image_id = db.Column(db.Text)
  ## RELATIONS
  # ONE TO MANY - Items
  items = db.relationship('Item', backref='category',lazy='dynamic')

  def __init__(self,name,image_id):
    self.name = name
    self.image_id = image_id

class Item(db.Model, SerializerMixin):
  __tablename__ = 'items'

  serialize_only = ('id', 'name', 'image_id', 'price', 'category_id')
  serialize_rules = ()

  ## ATTRIBUTES
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  image_id = db.Column(db.Text)
  price = db.Column(db.Float)
  category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

  def __init__(self,name,image_id,price):
    self.name = name
    self.image_id = image_id
    self.price = price

class Order(db.Model, SerializerMixin):
  __tablename__ = 'orders'

  serialize_only = ('id', 'created_at', 'items', 'payment', 'total')
  serialize_rules = ()

  ## ATTRIBUTES
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  items = db.Column(db.Text)
  payment = db.Column(db.Text)
  total = db.Column(db.Float)

  def __init__(self,items,payment,total):
    self.items = items
    self.payment = payment
    self.total = total