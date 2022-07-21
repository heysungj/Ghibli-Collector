from django.forms import ModelForm
from .models import Watching

class WatchForm(ModelForm):
  class Meta:
    model = Watching
    fields = ['date', 'time']