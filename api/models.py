import uuid

from django.db import models


class Movie(models.Model):
    id = models.UUIDField
    name = models.CharField(max_length=30)
    released_date = models.DateField()
    rating = models.FloatField(max_length=5)
    added_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
