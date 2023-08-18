import psycopg2
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = psycopg2.connect(database='catalog')

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM catalog_product')

            cursor.execute('DELETE FROM catalog_category')

        connection.commit()
        connection.close()

