from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'scem/welcome.html', {})

def come(request):
    return render(request, 'scem/way_to_come.html')

def bylaws(request):
    return render(request, 'scem/lab_bylaws.html')