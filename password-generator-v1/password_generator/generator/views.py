from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLAMNOPQRSTUVWXYZ'))

    if request.GET.get('special_characters'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    p = ''
    for x in range(length):
        p += random.choice(characters)

    context = {'password': p}
    return render(request, 'generator/password.html', context=context)

