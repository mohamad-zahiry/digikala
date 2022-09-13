import json

from requests import get

from .url_maker import URL_TYPES, url_maker_product_by_id


def __clean_details(details: list):
    _details = dict()
    for item in details:
        _details.update({item["title"]: item["values"]})
    return _details


def __clean_prodcuts_without_details(product_list):
    products = []
    for p in product_list:
        price = p.get("default_variant", 0)
        price = price["price"]["selling_price"] if price else 0
        products.append(
            {
                "product_id": p["id"],
                "exists": p["status"],
                "title_fa": p["id"],
                "price": price,
                "url": p["url"]["uri"],
            }
        )
    return products


def cleaner_category_brand(data: str, category: str = None, products_detail=True):
    data = json.loads(data)["data"]

    if products_detail:
        products = []
        for p in data["products"]:
            url = url_maker_product_by_id(p["id"])
            _data = get(url).text
            products.append(cleaner_product(_data))
    else:
        products = __clean_prodcuts_without_details(data["products"])

    return {
        "category": data["category"]["code"],
        "brand": data["brand"]["code"],
        "products": products,
    }


def cleaner_category(data: str, category: str, products_detail=True):
    if category == "mobile-phone":
        data = json.loads(data)["data"]["widgets"][8]["data"]["products"]
    elif category == "notebook-netbook-ultrabook":
        data = json.loads(data)["data"]["widgets"][1]["data"]["products"]
    else:
        raise Exception("Invalid category")

    if products_detail:
        products = []
        for p in data:
            url = url_maker_product_by_id(p["id"])
            _data = get(url).text
            products.append(cleaner_product(_data))
    else:
        products = __clean_prodcuts_without_details(products)

    return {
        "category": category,
        "products": products,
    }


def cleaner_product(data: str, category: str = None):
    data = json.loads(data)["data"]
    product = data["product"]
    price = product.get("default_variant", 0)
    price = price["price"]["rrp_price"] if price else 0
    off = product["default_variant"]["price"]["discount_percent"] if price else 0
    return {
        "brand": product["brand"]["code"],
        "title": product["title_fa"],
        "category": product["category"]["code"],
        "review": product["expert_reviews"]["description"],
        "product_id": product["id"],
        "details": __clean_details(product["specifications"][0]["attributes"]),
        "price": price,
        "off": off,
        "exists": product["status"],
        "url": product["url"]["uri"],
    }


def get_cleaner(url_type: str):
    if url_type == URL_TYPES.CATEGORY_BRAND:
        return cleaner_category_brand

    if url_type == URL_TYPES.CATEGORY:
        return cleaner_category

    if url_type == URL_TYPES.PRODUCT:
        return cleaner_product
