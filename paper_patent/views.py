from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'paper_patent/academic_journal_world.html', {})

def kor_jounal(request):
    return render(request, 'paper_patent/academic_journal_kor.html')

def world_conference(request):
    return render(request, 'paper_patent/academic_conference_world.html')

def kor_conference(request):
    return render(request, 'paper_patent/academic_conference_kor.html')

def world_thesis(request):
    return render(request, 'paper_patent/thesis_world.html')

def kor_thesis(request):
    return render(request, 'paper_patent/thesis_kor.html')

def property_1(request):
    return render(request, 'paper_patent/intellectual_property_1.html')

def property_2(request):
    return render(request, 'paper_patent/intellectual_property_2.html')

def property_3(request):
    return render(request, 'paper_patent/intellectual_property_3.html')