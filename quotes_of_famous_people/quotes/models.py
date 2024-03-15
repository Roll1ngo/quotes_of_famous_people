from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class AuthorDjango(models.Model):
    fullname = models.CharField(max_length=10000, null=False, unique=True)
    born_date = models.CharField(max_length=10000)
    born_location = models.CharField(max_length=50000)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.fullname


class QuoteDjango(models.Model):
    author = models.ForeignKey(AuthorDjango, on_delete=models.CASCADE)
    tags = models.JSONField()
    quote = models.CharField(max_length=10000)

    def __str__(self):
        return f"Author:{self.author}, tags:{self.tags}, quote:{self.quote}"
