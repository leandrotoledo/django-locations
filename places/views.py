from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from forms import *
import json

def location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            return True
    else:
        form = LocationForm()

    return render_to_response('location.html', {'form': form})

def get_countries(request):
    pass

def get_state(request, country):
    pass

def get_city(request, country, state):
    pass
