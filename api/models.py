import uuid

from django.db import models


class Movie(models.Model):
    id = models.UUIDField
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    screen_writer = models.CharField(max_length=30)
    release_year = models.IntegerField()
    rating = models.FloatField()
    rating_count =  models.IntegerField()
    genre = models.CharField(max_length=30)
    production_country = models.CharField(max_length=30)
    box_office = models.IntegerField(default=0)
    length = models.IntegerField()
    poster_url = models.CharField(max_length=30)

    def __str__(self):
        return self.title
