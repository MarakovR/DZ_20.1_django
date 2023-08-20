import json
from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('catalog_data.json', encoding='utf-8') as file:
            fixtures = json.load(file)
            fix_category = []
            fix_product = []

        Product.objects.all().delete()
        Category.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        for i in fixtures:
            if i['model'] == "catalog.product":
                fix_product.append(Product(
                    product_name=i['fields']['product_name'],
                    description=i['fields']['description'],
                    picture=i['fields']['picture'],
                    category_id=i['fields']['category'],
                    price=i['fields']['price'],
                    date_of_creation=i['fields']['date_of_creation'],
                    date_changes=i['fields']['date_changes']
                ))
            elif i['model'] == "catalog.category":
                fix_category.append(Category(
                    category_name=i['fields']['category_name'],
                    description=i['fields']['description']
                ))

        Category.objects.bulk_create(fix_category)
        Product.objects.bulk_create(fix_product)
