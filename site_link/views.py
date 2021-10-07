from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'site_link/CEM.html', {})

def public(request):
    return render(request, 'site_link/public.html')

def gov(request):
    return render(request, 'site_link/govment.html')

def insitute(request):
    return render(request, 'site_link/insitute.html')

def oversea(request):
    return render(request, 'site_link/oversea.html')

def other(request):
    return render(request, 'site_link/other.html')