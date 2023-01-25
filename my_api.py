from fastapi import FastAPI

api = FastAPI()

product_data = [
{"name": "headphones", "price":100.00, "catergory": "audio"},
{"name": "GPU", "price":1000.00, "catergory": "computing"},
{"name": "drone", "price":300.00, "catergory": "cameras"},
{"name": "gopro", "price":400.00, "catergory": "cameras"}
]

@api.get("/products")
def get_products(category: str, min_price: float):

    return product_data