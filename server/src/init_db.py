from api import db, Category, Item

db.create_all()

bakery = Category(name='Bakery', image_id='f3fbf57b118fa9')
entrees = Category(name='Entrees', image_id='b271afbefdc554')
drinks = Category(name='Drinks', image_id='eba73b2361fae3')

bakery.items.append(Item(name='Bagel',image_id='293202f9d9f7f4',price=2.0))
bakery.items.append(Item(name='Croissant',image_id='808916fd5ddf96',price=1.0))
bakery.items.append(Item(name='Muffin',image_id='95d02a230fe050',price=1.25))
bakery.items.append(Item(name='Toast / Bread',image_id='23f95765b967ff',price=1))
bakery.items.append(Item(name='English Muffin',image_id='5650be5d48a99b',price=2.5))

entrees.items.append(Item(name='Pasta Bar',image_id='bd237a0c0d19ef',price=12.99))
entrees.items.append(Item(name='Mediterranean Entree',image_id='3e1bd1342800f7',price=10.99))
entrees.items.append(Item(name='Indian Entree',image_id='72589c4c990f97',price=11.95))

drinks.items.append(Item(name='Small Drink',image_id='70c2a6247e7b58',price=0.75))
drinks.items.append(Item(name='Medium Drink',image_id='dba0fc03da30ca',price=1.5))
drinks.items.append(Item(name='Large Drink',image_id='ffc9bf61e441cd',price=2))

db.session.add_all([bakery, entrees, drinks])
db.session.commit()