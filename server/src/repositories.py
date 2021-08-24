import json

from models import db, Item, Order
from exceptions import BusinessException

def create_order(data):
  payment = json.dumps(data['payment'])
  items = json.dumps(data['items'])
  total = 0.0

  for item_id, count in data['items'].items():
    item = Item.query.get(item_id)
    if item == None:
      raise BusinessException('Invalid product on the list')

    total += (item.price * count)

  order = Order(items, payment, total)
  db.session.add(order)
  db.session.commit()

  return order