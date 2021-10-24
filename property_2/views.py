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
from .forms import property_2_form
from .models import property_2
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from urllib.parse import quote
import urllib
import mimetypes

def index(request):
    
    data_list = property_2.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 15)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page_num)

    context = {'data_list': page_obj, 'page': page}  # <------ so 추가
    return render(request, 'property_2/list.html', context)

@login_required(login_url='common:login')
def create(request):
    if request.method == "POST":
        form = property_2_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.FILES:
                post.filename = request.FILES['upload_files'].name
            post.save()
            return redirect('property_2:index')
        else:
            messages.error(request, 'Error!')
            return render(request,'property_2/test.html',{'form':form})
    else:
        form = property_2_form()
    return render(request, 'property_2/write.html', {'form':form})

def detail(request, pk):
    notice = get_object_or_404(property_2, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
    }

    return render(request, 'property_2/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    question = get_object_or_404(property_2, pk=pk)
    if request.method == "POST":
        file_change_check = request.POST.get('fileChange', False)
        file_check = request.POST.get('upload_files-clear', False)

        if file_check or file_change_check:
            os.remove(os.path.join(settings.MEDIA_ROOT, question.upload_files.path))

        form = property_2_form(request.POST, request.FILES,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('property_2:detail', pk=question.id)
    else:
        if request.user.username == 'admin' or request.user.username == 'cemuos':
            form = property_2_form(instance=question)
            context = {
                'form': form,
                'edit': '수정하기',
            }
            if question.filename and question.upload_files:
                context['filename'] = question.filename
                context['file_url'] = question.upload_files.url
            return render(request, "property_2/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/property_2/'+str(pk))
        
@login_required(login_url='common:login')
def delete(request, pk):
    notice = property_2.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('property_2:index')

def download(request, pk):
    notice = get_object_or_404(property_2, pk=pk)
    url = notice.upload_files.url[7:]
    print(type(url))
    print(url)
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(notice.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
