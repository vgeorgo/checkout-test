from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

from models import setup_db, Category, Item, Order
from repositories import create_order
from helpers import models_to_list
from exceptions import BusinessException

app = Flask(__name__)
cors = CORS(app)

setup_db(app)

@app.route("/menu", methods=['GET', 'OPTIONS'])
def get_menu():
  categories = models_to_list(Category.query.all())
  items = models_to_list(Item.query.all())

  return make_response(jsonify({
    'categories': categories,
    'items': items,
  }), 200)

@app.route("/orders", methods=['GET', 'OPTIONS'])
def get_orders():
  orders = models_to_list(Order.query.all())
  
  return make_response(jsonify(orders), 200)

@app.route("/orders", methods=['POST', 'OPTIONS'])
def post_orders():
  try:
    request_data = request.get_json()
    order = create_order(request_data)    

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