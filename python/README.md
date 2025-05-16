# Flask Product API

This is a simple Flask API for managing product data. The API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on products.

## Setup
To use this API, you need to have the following software installed on your system:

* Python 3.10 or later
* Flask
* Flask-RESTful
* Flask-Cors
* Peewee

You can install the required packages by running the following command:
```bash
pip install -r requirements.txt
```

# Usage

## db.py

### How to use
1. Open a terminal and navigate to the directory where db.py is located.
2. Run the script for create/update `products.db`  using the following command:
```bash
python db.py
```
* Use the following arguments to customize the script behavior:
```
-d, --delete_all_data: Deletes all existing product data.
-a, --add_default_data: Adds default product data to the database.
-p, --print_all_data: Prints all product data to the console.
```

## app.py
To run the API, execute the following command:
```bash
python app.py --host [HOST] --port [PORT]
```
Replace `[HOST]` with the IP address or hostname of the server and `[PORT]` with the port number you want to run the application on.

By default, the application will run on localhost and port 5000.

The API will then be accessible at http://localhost:5000.

### Endpoints

#### GET `/api/products`
Retrieves a list of all products in the database.

Example response:

```json
[
  {
    "id": 1,
    "name": "Sugar",
    "price": 32.0
  },
  {
    "id": 2,
    "name": "Sult",
    "price": 19.0
  },
  {
    "id": 3,
    "name": "Bread",
    "price": 20.0
  },
  {
    "id": 4,
    "name": "Butter",
    "price": 62.0
  },
  {
    "id": 5,
    "name": "Milk",
    "price": 32.0
  }
]
```

#### POST `/api/products`
Adds a new product to the database.

Example request body:
```json
{
  "name": "Eggs",
  "price": 12.0
}
```
Example response:
```json
{
  "message": "Product added successfully.",
  "productId": 6
}
```

#### GET `/api/products/{product_id}`
Retrieves a single product by ID.

Example response:
```json
{
  "id": 1,
  "name": "Sugar",
  "price": 32.0
}
```

#### PATCH `/api/products/{product_id}`
Updates a single product by ID.

Example request body:
```json
{
  "name": "Sugar (1kg)",
  "price": 35.0
}
```
Example response:
```json
{
  "message": "Product updated successfully."
}
```
#### DELETE `/api/products/{product_id}`
Deletes a single product by ID.

Example response:
```json
{
  "message": "Product deleted."
}
```



