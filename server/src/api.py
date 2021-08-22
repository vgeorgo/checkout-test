import json
from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/items", methods=['GET'])
def get_items():
  f = open('data/db.json')
  items = json.load(f)
  return make_response(jsonify(items), 200)

@app.route("/orders", methods=['POST'])
def post_orders():
  f = open('data/db.json')
  items = json.load(f)
  return make_response(jsonify(items), 200)

if __name__ == "__main__":
  app.run()