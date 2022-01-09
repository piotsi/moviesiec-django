import uuid

from django.db import models


class Movie(models.Model):
    id = models.UUIDField
    title = models.CharField(max_length=30, default="")
    director = models.CharField(max_length=30, default="")
    screen_writer = models.CharField(max_length=30, default="")
    release_year = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    rating_count =  models.IntegerField(default=0)
    genre = models.CharField(max_length=30, default="")
    production_country = models.CharField(max_length=30, default="")
    box_office = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    poster_url = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title
