from django.contrib import admin

# Register your models here.

from .models import Movie, Watching

admin.site.register(Movie)
# register the new Feeding Model 
admin.site.register(Watching)