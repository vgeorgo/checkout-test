# checkout-test

## Run
The only step is to have docker compose installed and run the command:
```
docker-compose up
```

## Store
Vue project that simulates an online shopping store.

URL: http://localhost:8080

The store is a single page application and consists in 4 steps:
- Choose: Pick every product that you wnat to buy
- Review: Show every selected item and its amount with the final order price
- Checkout: Input card information and creates the order
- Enjoy!: If the transaction was created successfully

## Server

Flask project connected to a SQLite database.

URL: http://localhost:5000

To simplify the application:
- Items and categories are already store in the database
- Payment and items are only being JSON encoded and saved with Order model

### Routes
#### Items
GET /items

Returns both items and categories:
```
{
  "categories": [
    {
      "id": 1,
      "image_id": "f3fbf57b118fa9",
      "name": "Bakery"
    }
    ...
  ],
  "items": [
    {
      "category_id": 1,
      "id": 1,
      "image_id": "293202f9d9f7f4",
      "name": "Bagel",
      "price": 2.0
    },
    ...
  ]
}
```

#### Orders
GET /orders

Returns every created order:
```
[
  {
    "created_at": "2021-08-23 02:12:01",
    "id": 1,
    "items": "{\"8\": 2, \"1\": 2, \"10\": 2}",
    "payment": "{\"card_number\": \"8888444433331111\", \"expiration\": \"05/25\", \"cv\": \"123\", \"owner\": \"John Doe\"}",
    "total": 0.0
  },
  ...
}
```

POST /orders

Receives payment and items data to create an order. Items are organized as ID: Count manner, so the server is able to calculate the total value of the order:
```
{
  "payment": {
    "card_number": "8888444433331111",
    "expiration": "05/25",
    "cv": "123",
    "owner": "John Doe"
  },
  "items": {
    "1": 3,
    "6": 2,
    "10": 2
  }
}
```