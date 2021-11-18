from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'research_pj/CM.html', {})

def PM(request):
    return render(request, 'research_pj/PM.html')

def VE(request):
    return render(request, 'research_pj/VE.html')

def Clame(request):
    return render(request, 'research_pj/Clame.html')

def PMIS(request):
    return render(request, 'research_pj/PMIS.html')

def EVMS(request):
    return render(request, 'research_pj/EVMS.html')

def Sustain(request):
    return render(request, 'research_pj/Sustain.html')

def RISK(request):
    return render(request, 'research_pj/RISK.html')

def QC(request):
    return render(request, 'research_pj/QC.html')

def DigitalTwin(request):
    return render(request, 'research_pj/DigitalTwin.html')

def AR(request):
    return render(request, 'reserch_pj/AR.html')