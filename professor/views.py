from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'professor/index.html')

def professor_Hyun(request):
    return render(request, 'professor/professor_Hyun.html')
    
def professor_Lee(request):
    return render(request, 'professor/professor_Lee.html')