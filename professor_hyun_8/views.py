from django.shortcuts import render

# Create your views here.
from datetime import timezone
# from django.core.checks import messages
from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import View, ListView, DetailView, FormView, CreateView
# Create your views here.
from django.http import HttpResponse
from .forms import professor_hyun_8_1_form, professor_hyun_8_2_form
from .models import professor_hyun_8_1, professor_hyun_8_2
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from urllib.parse import quote
import urllib
import mimetypes

def index(request):
    check_num = '8'
    check_num2 = '1'
    data_list = professor_hyun_8_1.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create(request):
    check_num = '8'
    check_num2 = '1'
    if request.method == "POST":
        form = professor_hyun_8_1_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_8:index')
    else:
        form = professor_hyun_8_1_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num, 'check_num2':check_num2})

def detail(request, pk):
    check_num = '8'
    check_num2 = '1'
    notice = get_object_or_404(professor_hyun_8_1, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    check_num = '8'
    check_num2 = '1'
    question = get_object_or_404(professor_hyun_8_1, pk=pk)
    if request.method == "POST":
        form = professor_hyun_8_1_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_8:detail', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_8_1_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_8/'+str(pk))
        
@login_required(login_url='common:login')
def delete(request, pk):
    notice = professor_hyun_8_1.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_8:index')

def index_2(request):
    check_num = '8'
    check_num2 = '2'
    data_list = professor_hyun_8_2.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create_2(request):
    check_num = '8'
    check_num2 = '2'
    if request.method == "POST":
        form = professor_hyun_8_2_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_8:index_2')
    else:
        form = professor_hyun_8_2_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num,'check_num2':check_num2})

def detail_2(request, pk):
    check_num = '8'
    check_num2 = '2'
    notice = get_object_or_404(professor_hyun_8_2, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update_2(request,pk):
    check_num = '8'
    check_num2 = '2'
    question = get_object_or_404(professor_hyun_8_2, pk=pk)
    if request.method == "POST":
        form = professor_hyun_8_2_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_8:detail_2', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_8_2_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_8/'+str(pk)+'/great')
        
@login_required(login_url='common:login')
def delete_2(request, pk):
    notice = professor_hyun_8_2.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_8:index_2')