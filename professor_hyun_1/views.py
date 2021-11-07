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
from .forms import professor_hyun_1_1_form, professor_hyun_1_2_form, professor_hyun_1_3_form, professor_hyun_1_4_form, professor_hyun_1_5_form
from .models import professor_hyun_1_1, professor_hyun_1_2, professor_hyun_1_3, professor_hyun_1_4, professor_hyun_1_5
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from urllib.parse import quote
import urllib
import mimetypes

def index(request):
    check_num = '1'
    check_num2 = '1'
    data_list = professor_hyun_1_1.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create(request):
    check_num = '1'
    check_num2 = '1'
    if request.method == "POST":
        form = professor_hyun_1_1_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_1:index')
    else:
        form = professor_hyun_1_1_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num, 'check_num2':check_num2})

def detail(request, pk):
    check_num = '1'
    check_num2 = '1'
    notice = get_object_or_404(professor_hyun_1_1, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    check_num = '1'
    check_num2 = '1'
    question = get_object_or_404(professor_hyun_1_1, pk=pk)
    if request.method == "POST":
        form = professor_hyun_1_1_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_1:detail', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_1_1_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_1/'+str(pk))
        
@login_required(login_url='common:login')
def delete(request, pk):
    notice = professor_hyun_1_1.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_1:index')

def index_2(request):
    check_num = '1'
    check_num2 = '2'
    data_list = professor_hyun_1_2.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create_2(request):
    check_num = '1'
    check_num2 = '2'
    if request.method == "POST":
        form = professor_hyun_1_2_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_1:index_2')
    else:
        form = professor_hyun_1_2_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num,'check_num2':check_num2})

def detail_2(request, pk):
    check_num = '1'
    check_num2 = '2'
    notice = get_object_or_404(professor_hyun_1_2, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update_2(request,pk):
    check_num = '1'
    check_num2 = '2'
    question = get_object_or_404(professor_hyun_1_2, pk=pk)
    if request.method == "POST":
        form = professor_hyun_1_2_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_1:detail_2', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_1_2_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_1/'+str(pk)+'/thesis')
        
@login_required(login_url='common:login')
def delete_2(request, pk):
    notice = professor_hyun_1_2.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_1:index_2')

def index_3(request):
    check_num = '1'
    check_num2 = '3'
    data_list = professor_hyun_1_3.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create_3(request):
    check_num = '1'
    check_num2 = '3'
    if request.method == "POST":
        form = professor_hyun_1_3_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_1:index_3')
    else:
        form = professor_hyun_1_3_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num,'check_num2':check_num2})

def detail_3(request, pk):
    check_num = '1'
    check_num2 = '3'
    notice = get_object_or_404(professor_hyun_1_3, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update_3(request,pk):
    check_num = '1'
    check_num2 = '3'
    question = get_object_or_404(professor_hyun_1_3, pk=pk)
    if request.method == "POST":
        form = professor_hyun_1_3_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_1:detail_3', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_1_3_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_1/'+str(pk)+'/academic')
        
@login_required(login_url='common:login')
def delete_3(request, pk):
    notice = professor_hyun_1_3.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_1:index_3')

def index_4(request):
    check_num = '1'
    check_num2 = '4'
    data_list = professor_hyun_1_4.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create_4(request):
    check_num = '1'
    check_num2 = '4'
    if request.method == "POST":
        form = professor_hyun_1_4_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_1:index_4')
    else:
        form = professor_hyun_1_4_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num,'check_num2':check_num2})

def detail_4(request, pk):
    check_num = '1'
    check_num2 = '4'
    notice = get_object_or_404(professor_hyun_1_4, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update_4(request,pk):
    check_num = '1'
    check_num2 = '4'
    question = get_object_or_404(professor_hyun_1_4, pk=pk)
    if request.method == "POST":
        form = professor_hyun_1_4_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_1:detail_4', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_1_4_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_1/'+str(pk)+'/world_conf')
        
@login_required(login_url='common:login')
def delete_4(request, pk):
    notice = professor_hyun_1_4.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_1:index_4')

def index_5(request):
    check_num = '1'
    check_num2 = '5'
    data_list = professor_hyun_1_5.objects.all().order_by('-id')
    context = {'data_list': data_list, 'check_num': check_num,'check_num2':check_num2}  # <------ so 추가
    return render(request, 'professor/professor_Hyun/list.html', context)

@login_required(login_url='common:login')
def create_5(request):
    check_num = '1'
    check_num2 = '5'
    if request.method == "POST":
        form = professor_hyun_1_5_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('professor_hyun_1:index_5')
    else:
        form = professor_hyun_1_5_form()
    return render(request, 'professor/professor_Hyun/write.html', {'form':form, 'check_num':check_num,'check_num2':check_num2})

def detail_5(request, pk):
    check_num = '1'
    check_num2 = '5'
    notice = get_object_or_404(professor_hyun_1_5, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
        'check_num2':check_num2,
    }

    return render(request, 'professor/professor_Hyun/detail.html', context)

@login_required(login_url='common:login')
def update_5(request,pk):
    check_num = '1'
    check_num2 = '5'
    question = get_object_or_404(professor_hyun_1_5, pk=pk)
    if request.method == "POST":
        form = professor_hyun_1_5_form(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('professor_hyun_1:detail_5', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = professor_hyun_1_5_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
                'check_num2': check_num2,
            }
            return render(request, "professor/professor_Hyun/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/professor_hyun_1/'+str(pk)+'/kor_conf')
        
@login_required(login_url='common:login')
def delete_5(request, pk):
    notice = professor_hyun_1_5.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('professor_hyun_1:index_5')