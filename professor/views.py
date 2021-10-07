from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'professor/index.html')

def professor_Hyun(request):
    return render(request, 'professor/1.html')
    
def professor_Lee(request):
    return render(request, 'professor/2.html')