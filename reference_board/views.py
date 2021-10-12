from datetime import timezone
# from django.core.checks import messages
from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import View, ListView, DetailView, FormView, CreateView
# Create your views here.
from django.http import HttpResponse
from .forms import ReferenceForm
from .models import DataRoom
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings

def index(request):
    
    data_list = DataRoom.objects.all().order_by('-id')

    # 페이징처리
    paginator = Paginator(data_list, 5)  # 페이지당 10개씩 보여주기
    page_num = request.GET.get('page', '1')  # 페이지
    try :
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)
        
    page_obj = paginator.get_page(page)

    context = {'data_list': page_obj, 'page': page}  # <------ so 추가
    return render(request, 'reference_board/list.html', context)

@login_required(login_url='common:login')
def create(request):
    if request.method == "POST":
        form = ReferenceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.FILES:
                post.filename = request.FILES['upload_files'].name
            post.save()
            return redirect('ref_room:index')
        else:
            messages.error(request, 'Error!')
            return render(request,'reference_board/test.html',{'form':form})
    else:
        form = ReferenceForm()
    return render(request, 'reference_board/write.html', {'form':form})

def detail(request, pk):
    notice = get_object_or_404(DataRoom, pk=pk)
    # notice = Notice.objects.filter(id=pk)
    context = {
        'notice': notice,
    }

    return render(request, 'reference_board/detail.html', context)

@login_required(login_url='common:login')
def update(request,pk):
    question = get_object_or_404(DataRoom, pk=pk)
    if request.method == "POST":
        form = ReferenceForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('ref_room:detail', pk=question.id)
    else:
        form = ReferenceForm(instance=question)
    context = {'form': form, 'edit':'수정하기'}
    return render(request, 'reference_board/write.html', context)

def notice_edit_view(request, pk):
    notice = DataRoom.objects.get(id=pk)

    if request.method == "POST":
        if(request.user.username == 'admin' or request.user.username == 'cemuos'):

            # file_change_check = request.POST.get('fileChange', False)
            # file_check = request.POST.get('upload_files-clear', False)
            
            # if file_check or file_change_check:
            #     os.remove(os.path.join(settings.MEDIA_ROOT, notice.upload_files.path))

            form = ReferenceForm(request.POST, request.FILES, instance=notice)
            if form.is_valid():
                # test-------------------------------#
                notice = form.save(commit = False)
                if request.FILES:
                    if 'upload_files' in request.FILES.keys():
                        notice.filename = request.FILES['upload_files'].name
                notice.save()
                #------------------------------------#
                # form.save()
                messages.success(request, "수정되었습니다.")
                return redirect('/ref_room/'+str(pk))
    else:
        notice = DataRoom.objects.get(id=pk)
        if notice.writer == request.user:
            form = ReferenceForm(instance=notice)
            # test---------------------------------------------------------#
            context = {
                'form': form,
                'edit': '수정하기',
            }
            if notice.filename and notice.upload_files:
                context['filename'] = notice.filename
                context['file_url'] = notice.upload_files.url
            #--------------------------------------------------------------#
            return render(request, "reference_board/write.html", context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/ref_room/'+str(pk))

@login_required(login_url='common:login')
def delete(request, pk):
    notice = DataRoom.objects.get(id=pk)
    if request.user.username == 'cemuos' or request.user.username == 'admin':
        notice.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('ref_room:index')

def download(request, pk):
    file = get_object_or_404(DataRoom, pk=pk)
    file_url = file.upload_files.url[7:]
    if os.path.exists(file_url):
        with open(file_url,'rb') as fh:
            response = HttpResponse(fh.read(), content_type="")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_url)
            return response
    raise Http404
