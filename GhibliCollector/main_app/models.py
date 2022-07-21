from django.db import models
# Import the reverse function
from django.urls import reverse
# Create your models here.
from datetime import date

TIME = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release = models.IntegerField()
    director = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    # new code below
    def __str__(self):
        return self.name
    #  reverse to url 'detail' and with cat_id
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

class Watching(models.Model):

    date = models.DateField('Watched Date')
    time = models.CharField(
        'Watch Time',
        max_length=1,
        choices=TIME,
        default=TIME[0][0]
    )
    # create a movie_id column in the db
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']