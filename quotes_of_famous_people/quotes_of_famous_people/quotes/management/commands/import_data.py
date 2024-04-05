from pymongo import MongoClient

from django.core.management.base import BaseCommand

from ...models import AuthorDjango, QuoteDjango

client = MongoClient("mongodb+srv://Vladislav_B:dIvg5BCNadnWGk7E@hwmongobase.o1jywze.mongodb.net/")
db = client['HWMongoDB']
authors = db['authors']
quotes = db['quotes']


class Command(BaseCommand):
    help = 'Import data from Mongo in PostgreSQL'

    def handle(self, *args, **kwargs):
        """Import data from Mongo in PostgreSQL"""

        documents = authors.find()
        for row in documents:
            author = AuthorDjango(fullname=row.get('fullname'),
                                  born_date=row.get('born_date'),
                                  born_location=row.get('born_location'),
                                  description=row.get('description')
                                  )
            author.save()

        documents_quotes = quotes.find()
        for row in documents_quotes:
            author_id_quotes = row.get('author')
            documents = authors.find()
            for doc in documents:
                author_name = doc.get('fullname')
                if author_id_quotes == doc.get('_id'):
                    quote = QuoteDjango(
                        author=AuthorDjango.objects.get(fullname=author_name),
                        tags=row.get('tags'),
                        quote=row.get('quote')
                    )
                    quote.save()
