from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release = models.IntegerField()
    director = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    # new code below
    def __str__(self):
        return self.name