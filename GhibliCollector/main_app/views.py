from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Movie:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, release, director, music):
    self.name = name
    self.release = release
    self.director = director
    self.music = music

movies = [
  Movie('Ponyo', '2008', 'Hayao Miyazaki', 'Joe Hisaishi'),
  Movie('Spirited Away', '2001', 'Hayao Miyazaki', 'Joe Hisaishi'),
  Movie('My Neighbor Totoro', '1988', 'Hayao Miyazaki', 'Joe Hisaishi')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

# Add new view
def movies_index(request):
  return render(request, 'movies/index.html', { 'movies': movies })