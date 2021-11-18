from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.
from django.http import HttpResponse

from site_link.models import Sitelink, Sitelink_2, Sitelink_3, Sitelink_4, Sitelink_5, Sitelink_6
from site_link.forms import Sitelink_form, Sitelink_form_2, Sitelink_form_3, Sitelink_form_4, Sitelink_form_5, Sitelink_form_6

def CEM(request):
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

def index(request):
    check_num = '1'
    data_list = Sitelink.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page,'check_num':check_num}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create(request):
    check_num = '1'
    if request.method == "POST":
        form = Sitelink_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form,'check_num':check_num})
    else:
        form = Sitelink_form()
    return render(request, 'Sitelink/write.html', {'form':form,'check_num':check_num})

def detail(request, pk):
    notice = get_object_or_404(Sitelink, pk=pk)
    check_num = '1'
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    question = get_object_or_404(Sitelink, pk=pk)
    check_num = '1'
    if request.method == "POST":
        form = Sitelink_form(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('site_link:detail', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Sitelink_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num':check_num,
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk))
        
@login_required(login_url='common:login')
def delete(request, pk):
    notice = Sitelink.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index')

def index_2(request):
    check_num = '2'
    data_list = Sitelink_2.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page,'check_num':check_num}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create_2(request):
    check_num = '2'
    if request.method == "POST":
        form = Sitelink_form_2(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index_2')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form,'check_num':check_num})
    else:
        form = Sitelink_form_2()
    return render(request, 'Sitelink/write.html', {'form':form,'check_num':check_num})

def detail_2(request, pk):
    notice = get_object_or_404(Sitelink_2, pk=pk)
    check_num = '2'
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update_2(request,pk):
    question = get_object_or_404(Sitelink_2, pk=pk)
    check_num = '2'
    if request.method == "POST":
        form = Sitelink_form_2(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('site_link:detail_2', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Sitelink_form_2(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num':check_num
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk)+'/public')
        
@login_required(login_url='common:login')
def delete_2(request, pk):
    notice = Sitelink_2.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index_2')

def index_3(request):
    check_num = '3'
    data_list = Sitelink_3.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page, 'check_num':check_num}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create_3(request):
    check_num = '3'
    if request.method == "POST":
        form = Sitelink_form_3(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index_3')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form,'check_num':check_num})
    else:
        form = Sitelink_form_3()
    return render(request, 'Sitelink/write.html', {'form':form,'check_num':check_num})

def detail_3(request, pk):
    notice = get_object_or_404(Sitelink_3, pk=pk)
    check_num = '3'
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update_3(request,pk):
    question = get_object_or_404(Sitelink_3, pk=pk)
    check_num = '3'
    if request.method == "POST":
        form = Sitelink_form_3(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('site_link:detail_3', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Sitelink_form_3(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num':check_num
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk)+'/gov')
        
@login_required(login_url='common:login')
def delete_3(request, pk):
    notice = Sitelink_3.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index_3')

def index_4(request):
    check_num = '4'
    data_list = Sitelink_4.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page, 'check_num':check_num}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create_4(request):
    check_num = '4'
    if request.method == "POST":
        form = Sitelink_form_4(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index_4')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form,'check_num':check_num})
    else:
        form = Sitelink_form_4()
    return render(request, 'Sitelink/write.html', {'form':form,'check_num':check_num})

def detail_4(request, pk):
    notice = get_object_or_404(Sitelink_4, pk=pk)
    check_num = '4'
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num,
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update_4(request,pk):
    question = get_object_or_404(Sitelink_4, pk=pk)
    check_num = '4'
    if request.method == "POST":
        form = Sitelink_form_4(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('site_link:detail_4', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Sitelink_form_4(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num':check_num,
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk)+'/insitute')
        
@login_required(login_url='common:login')
def delete_4(request, pk):
    notice = Sitelink_4.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index_4')

def index_5(request):
    check_num = '5'
    data_list = Sitelink_5.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page,'check_num':check_num}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create_5(request):
    check_num = '5'
    if request.method == "POST":
        form = Sitelink_form_5(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index_5')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form,'check_num':check_num})
    else:
        form = Sitelink_form_5()
    return render(request, 'Sitelink/write.html', {'form':form,'check_num':check_num})

def detail_5(request, pk):
    notice = get_object_or_404(Sitelink_5, pk=pk)
    check_num = '5'
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update_5(request,pk):
    question = get_object_or_404(Sitelink_5, pk=pk)
    check_num = '5'
    if request.method == "POST":
        form = Sitelink_form_5(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('site_link:detail_5', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Sitelink_form_5(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk)+'/oversea')
        
@login_required(login_url='common:login')
def delete_5(request, pk):
    notice = Sitelink_5.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index_5')

def index_6(request):
    check_num = '6'
    data_list = Sitelink_6.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page, 'check_num':check_num}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create_6(request):
    check_num = '6'
    if request.method == "POST":
        form = Sitelink_form_6(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index_6')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form,'check_num':check_num})
    else:
        form = Sitelink_form_6()
    return render(request, 'Sitelink/write.html', {'form':form,'check_num':check_num})

def detail_6(request, pk):
    notice = get_object_or_404(Sitelink_6, pk=pk)
    check_num = '6'
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
        'check_num':check_num
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update_6(request,pk):
    question = get_object_or_404(Sitelink_6, pk=pk)
    check_num = '6'
    if request.method == "POST":
        form = Sitelink_form_6(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('site_link:detail_6', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Sitelink_form_6(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
                'check_num': check_num,
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk)+'/other')
        
@login_required(login_url='common:login')
def delete_6(request, pk):
    notice = Sitelink_6.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index_6')
