from django.forms import ModelForm
from . import models


class TodoForm(ModelForm):

    class Meta:
        model = models.Todo
        fields = ['title', 'memo', 'important']

