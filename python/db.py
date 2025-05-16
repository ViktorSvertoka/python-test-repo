from peewee import *
import argparse

# Define the database and the model
db = SqliteDatabase('products.db')


class ProductModel(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    price = IntegerField()

    class Meta:
        database = db
        db_table = 'product'

    def __str__(self):
        return f"({self.id}, {self.name}, {self.price})"

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "price": self.price}


# Create a new product
def create_product(name, price):
    product = ProductModel(name=name, price=price)
    product.save()
    return product


# Retrieve a product by ID
def get_product_by_id(product_id):
    try:
        product = ProductModel.get(ProductModel.id == product_id)
        return product
    except DoesNotExist:
        return None


# Update a product by ID
def update_product(product_id, name=None, price=None):
    product = get_product_by_id(product_id)
    if product:
        if name:
            product.name = name
        if price:
            product.price = price
        product.save()
        return product
    else:
        return None


# Delete a product by ID
def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        product.delete_instance()
        return True
    else:
        return False


def _add_default_data():
    create_product("Sugar", 32)
    create_product("Sult", 19)
    create_product("Bread", 20)
    create_product("Butter", 62)
    create_product("Milk", 32)


def _print_all_data():
    for row in ProductModel.select():
        print(row)


if __name__ == "__main__":
    # Create the table
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delete_all_data', help='deletes all data', action='store_true')
    parser.add_argument('-a', '--add_default_data', help='add default data', action='store_true')
    parser.add_argument('-p', '--print_all_data', help='print all rows', action='store_true')
    args = parser.parse_args()

    db.create_tables([ProductModel])

    if args.delete_all_data:
        ProductModel.delete().execute()
    if args.add_default_data:
        _add_default_data()
    if args.print_all_data:
        _print_all_data()
