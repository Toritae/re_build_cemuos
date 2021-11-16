from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.
from django.http import HttpResponse

from site_link.models import Sitelink
from site_link.forms import Sitelink_form

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
    
    data_list = Sitelink.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page}  # <------ so 추가
    return render(request, 'Sitelink/list.html', context)

@login_required(login_url='common:login')
def create(request):
    if request.method == "POST":
        form = Sitelink_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('site_link:index')
        else:
            messages.error(request, 'Error!')
            return render(request,'Sitelink/test.html',{'form':form})
    else:
        form = Sitelink_form()
    return render(request, 'Sitelink/write.html', {'form':form})

def detail(request, pk):
    notice = get_object_or_404(Sitelink, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
    }

    return render(request, 'Sitelink/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    question = get_object_or_404(Sitelink, pk=pk)
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
            }
            return render(request, "Sitelink/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/site_link/'+str(pk))
        
@login_required(login_url='common:login')
def delete(request, pk):
    notice = Sitelink.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        messages.success(request, "삭제되었습니다.")
        return redirect('site_link:index')
