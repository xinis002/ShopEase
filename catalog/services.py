from django.core.cache import cache
from catalog.models import Product
from config.settings import CASH_ENABLED

def get_products_from_cache():
    if not CASH_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


