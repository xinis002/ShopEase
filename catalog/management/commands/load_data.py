import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/categories_data.json', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('fixtures/products_data.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()


        categories_data = self.json_read_categories()
        category_for_create = []
        for item in categories_data:
            fields = item['fields']
            category_for_create.append(Category(
                id=item['pk'],
                name=fields['name'],
                description=fields['description'],
            ))
        Category.objects.bulk_create(category_for_create)


        products_data = self.json_read_products()
        product_for_create = []
        for item in products_data:
            fields = item['fields']
            product_for_create.append(Product(
                id=item['pk'],
                name=fields['name'],
                description=fields['description'],
                image=fields['image'],
                category=Category.objects.get(pk=fields['category']),
                price=fields['price'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at'],
                manufactured_at=fields['manufactured_at']
            ))
        Product.objects.bulk_create(product_for_create)
