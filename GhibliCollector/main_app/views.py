from django.shortcuts import render, redirect
from .models import Movie, Actor
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import WatchForm
from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

# Add new view
def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  # Get the toys the cat doesn't have...
  # First, create a list of the toy ids that the cat DOES have
  id_list = movie.actors.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  actors_movie_doesnt_have = Actor.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in the template
  watching_form = WatchForm()
  return render(request, 'movies/detail.html', 
    { 'movie': movie, 'watching_form': watching_form, 'actors': actors_movie_doesnt_have })

def assoc_actor(request, movie_id, actor_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Movie.objects.get(id=movie_id).actors.add(actor_id)
  return redirect('detail', movie_id=movie_id)

def add_watching(request, movie_id):
  # create a ModelForm instance using the data in request.POST
  form = WatchForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_watching = form.save(commit=False)
    new_watching .movie_id = movie_id
    new_watching .save()
  return redirect('detail', movie_id=movie_id)

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'
  success_url = '/movies/'

class MovieUpdate(UpdateView):
  model = Movie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['release', 'director', 'music']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'


class ActorList(ListView):
  model = Actor

class ActorDetail(DetailView):
  model = Actor

class ActorCreate(CreateView):
  model = Actor
  fields = '__all__'
  success_url = '/actors/'


class ActorUpdate(UpdateView):
  model = Actor
  fields = ['name']

class ActorDelete(DeleteView):
  model = Actor
  success_url = '/actors/'