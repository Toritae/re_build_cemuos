from datetime import timezone
# from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import View, ListView, DetailView, FormView, CreateView
# Create your views here.
from django.http import HttpResponse
from .forms import PostForm
from .models import pj_post_gov
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
def index(request):
    
    data_list = pj_post_gov.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 5)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page)

    context = {'data_list': page_obj, 'page': page}  # <------ so 추가
    return render(request, 'pj_board_gov/board_list.html', context)

@login_required(login_url='common:login')
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' not in request.FILES.keys():
                return redirect('pj_board_gov:create')
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('pj_board_gov:index')
        else:
            messages.error(request, 'Error!')
            return render(request,'pj_board_gov/test.html',{'form':form})
    else:
        form = PostForm()
    return render(request, 'pj_board_gov/create.html', {'form':form})

def detail(request, pk):
    notice = get_object_or_404(pj_post_gov, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
    }

    return render(request, 'pj_board_gov/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    question = get_object_or_404(pj_post_gov, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=question)
        if form.is_valid():
            if 'photo' not in request.FILES.keys():
                return redirect('pj_board_gov:update',pk)
            question = form.save(commit=False)
            question.save()
            return redirect('pj_board_gov:detail', pk=question.id)
    else:
        form = PostForm(instance=question)
    context = {'form': form, 'edit':'수정하기'}
    return render(request, 'pj_board_gov/create.html', context)

def notice_edit_view(request, pk):
    notice = get_object_or_404(pj_post_gov, pk=pk)
    if request.method == "POST":
        file_check = request.POST.get('Photo', False)
        form = PostForm(request.POST, request.FILES, instance=notice)

        if file_check:
            os.remove(os.path.join(settings.MEDIA_ROOT, notice.upload_files.path))

        if form.is_valid():
            # test-------------------------------#
            notice = form.save(commit = False)
            notice.save()
            #------------------------------------#
            # form.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/pj_board_gov/'+str(pk))
    else:
        form = PostForm(request.POST, request.FILES, instance=notice)
    return render(request, 'pj_board_gov/create.html', {'form':form, 'edit':'수정하기'})
            
    

@login_required(login_url='common:login')
def delete(request, pk):
    notice = pj_post_gov.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('pj_board_gov:index')
