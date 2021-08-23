import json
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

from models import setup_db, db, Category, Item, Order
from exceptions import BusinessException

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

setup_db(app)

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