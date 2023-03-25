from fastapi import FastAPI
from firebase_admin import credentials, db, initialize_app
from typing import List

app = FastAPI()

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)

@app.get("/")
async def root():
    return {"message": "Welcome to the fruit and vegetable store!"}

@app.get("/products")
async def get_products():
    # Get a reference to the "products" node in the database
    ref = db.reference('products')
    # Get all the products
    products = ref.get()
    # Convert the dictionary of products to a list
    product_list = [product for product in products.values()]
    return product_list

@app.post("/checkout")
async def checkout(items: List[dict]):
    # Calculate the total price of the items
    total_price = sum(item['price'] * item['quantity'] for item in items)
    #  implement checkout logic, e.g. create a Stripe charge
    return {"message": f"Your order total is {total_price}."}
