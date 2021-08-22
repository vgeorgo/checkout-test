import os
import datetime
import json
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data', 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)

class Category(db.Model, SerializerMixin):
  # override tablename [optional]
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
  # override tablename [optional]
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
  # override tablename [optional]
  __tablename__ = 'orders'

  ## ATTRIBUTES
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  items = db.Column(db.Text)
  total = db.Column(db.Float)

  def __init__(self,name,items,total):
    self.name = name
    self.items = items
    self.total = total


@app.route("/items", methods=['GET'])
def get_items():
  categories = list(map(lambda c: c.to_dict(), Category.query.all()))
  items = list(map(lambda i: i.to_dict(), Item.query.all()))

  return make_response(jsonify({
    'categories': categories,
    'items': items,
  }), 200)

@app.route("/orders", methods=['POST'])
def post_orders():
  f = open('data/db.json')
  items = json.load(f)
  return make_response(jsonify(items), 200)