from inspect import isclass
from unicodedata import category
from requests import get

from .url_maker import URL_TYPES, get_url_maker, is_category, get_product_id
from .cleaner import get_cleaner


def get_url_cleaned_data(url: str):
    url_type, url_maker = get_url_maker(url)

    category = ""
    if url_type == URL_TYPES.CATEGORY:
        category = is_category(url)

    data = get(url_maker(url)).text
    cleaner = get_cleaner(url_type)
    return cleaner(data, category=category)
