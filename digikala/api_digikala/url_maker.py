import re

API_URL = "https://api.digikala.com/v1"


class URL_TYPES:
    CATEGORY_BRAND = "CB"
    CATEGORY = "C"
    PRODUCT = "P"


def is_category_brand(url: str):
    match = re.match(r"^https://www\.digikala\.com/search/category-([\w-]+)/([\w]+)/$", url)
    return (match.group(1), match.group(2)) if match is not None else match


def is_category(url: str):
    match = re.match(r"^https://www\.digikala\.com/search/category-([\w-]+)/$", url)
    return match.group(1) if match is not None else match


def is_product(url: str):
    match = re.match(r"^https://www\.digikala\.com/product/dkp-([\d]+)/.*$", url)
    return match.group(1) if match is not None else match


get_product_id = is_product


def url_maker_category_brand(url: str):
    category, brand = is_category_brand(url)
    return f"{API_URL}/categories/{category}/brands/{brand}/search/"


def url_maker_category(url: str):
    return f"{API_URL}/dynamic-category-page/{is_category(url)}/"


def url_maker_product(url: str):
    return f"{API_URL}/product/{is_product(url)}/"


def url_maker_product_by_id(id: str):
    return f"{API_URL}/product/{id}/"


def get_url_maker(url: str):
    if is_category_brand(url):
        return (URL_TYPES.CATEGORY_BRAND, url_maker_category_brand)

    if is_category(url):
        return (URL_TYPES.CATEGORY, url_maker_category)

    if is_product(url):
        return (URL_TYPES.PRODUCT, url_maker_product)

    raise Exception(f"'{url}' is not supported or invalid")


def convert_to_api(url: str):
    try:
        _, func = get_url_maker(url)
        return func(url)
    except Exception:
        raise Exception(f"'{url}' is not supported or invalid")
