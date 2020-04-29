from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    projects = models.Project.objects.all()
    return render(request, 'portfolio/home.html', {"projects": projects})

