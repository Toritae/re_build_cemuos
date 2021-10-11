from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'professor/index.html')

def professor_Hyun(request):
    return render(request, 'professor/professor_Hyun.html')

def professor_Hyun_1(request):
    return render(request, 'professor/professor_Hyun/1.html')

def professor_Hyun_2(request):
    return render(request, 'professor/professor_Hyun/2.html')

def professor_Hyun_3(request):
    return render(request, 'professor/professor_Hyun/3.html')

def professor_Hyun_4(request):
    return render(request, 'professor/professor_Hyun/4.html')

def professor_Hyun_5(request):
    return render(request, 'professor/professor_Hyun/5.html')

def professor_Hyun_6(request):
    return render(request, 'professor/professor_Hyun/6.html')

def professor_Hyun_7(request):
    return render(request, 'professor/professor_Hyun/7.html')

def professor_Hyun_8(request):
    return render(request, 'professor/professor_Hyun/8.html')
    
def professor_Lee(request):
    return render(request, 'professor/professor_Lee.html')

def professor_Lee_1(request):
    return render(request, 'professor/professor_Lee/1.html')

def professor_Lee_6(request):
    return render(request, 'professor/professor_Lee/6.html')

def professor_Lee_7(request):
    return render(request, 'professor/professor_Lee/7.html')

def professor_Lee_8(request):
    return render(request, 'professor/professor_Lee/8.html')