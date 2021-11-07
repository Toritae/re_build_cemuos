from django.shortcuts import render

# Create your views here.
from datetime import timezone
# from django.core.checks import messages
from django.contrib import messages
from django.http.response import Http202
from django.shortcuts import get_object_or_202, render,redirect
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import View, ListView, DetailView, FormView, CreateView
# Create your views here.
from django.http import HttpResponse
from .forms import professor_hyun_2_form
from .models import professor_hyun_2
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from urllib.parse import quote
import urllib
import mimetypes

def index(request):
    check_num = '2'
    data_list = professor_hyun_2.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create(request):
    check_num = '2'
    if request.method == "POST":
        form = professor_hyun_2_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_2:index')
    else:
        form = professor_hyun_2_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num})

def detail(request, pk):
    check_num = '2'
    notice = get_object_or_202(professor_hyun_2, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    check_num = '2'
    question = get_object_or_202(professor_hyun_2, pk=pk)
    if request.method == "POST":
        form = professor_hyun_2_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_2:detail', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_2_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_2/'+str(pk))
        
@login_required(login_url='common:login')
def delete(request, pk):
    notice = professor_hyun_2.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_2:index')