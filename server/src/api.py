import os
import datetime
import json
from flask import Flask, jsonify, make_response, request
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


@app.route("/items", methods=['GET'])
def get_items():
  categories = list(map(lambda c: c.to_dict(), Category.query.all()))
  items = list(map(lambda i: i.to_dict(), Item.query.all()))

  return make_response(jsonify({
    'categories': categories,
    'items': items,
  }), 200)

@app.route("/orders", methods=['GET'])
def get_orders():
  orders = list(map(lambda o: o.to_dict(), Order.query.all()))
  
  return make_response(jsonify(orders), 200)

class BusinessException(Exception):
  pass

@app.route("/orders", methods=['POST'])
def post_orders():
  try:
    request_data = request.get_json()

    payment = json.dumps(request_data['payment'])
    items = json.dumps(request_data['items'])
    total = 0.0

    for item_id, count in request_data['items'].items():
      item = Item.query.get(item_id)
      if item == None:
        raise BusinessException('Invalid product on the list')

      total += (item.price * count)

    order = Order(items, payment, total)
    db.session.add(order)
    db.session.commit()

    return make_response(jsonify(order.to_dict()), 200)
  except (BusinessException) as err:
    return make_response(jsonify({
      'message': "{0}".format(err)
    }), 422)
  except (RuntimeError, TypeError, NameError) as err:
    return make_response(jsonify({
      'message': 'There was a problem with your request',
      'detail': "{0}".format(err)
    }), 500)

if __name__ == '__main__':
    app.run(port=5000, debug=True)