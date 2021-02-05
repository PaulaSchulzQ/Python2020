from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from django.shortcuts import render
from django.utils.crypto import get_random_string


def index(request):
    request.session['counter'] = 0
    return render(request, 'aleat.html')

def funct_session(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

def random_word(request):
    request.session['counter'] += 1
    context = {
        "word": get_random_string(length=14)
    }
    return render(request, 'aleat.html', context)