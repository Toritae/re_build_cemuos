from django.shortcuts import render, get_object_or_404, redirect, resolve_url
# from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DetailView, FormView, CreateView
from .models import Q_A, Q_A_Answer
from django.db.models import QA
from django.contrib import messages
from django.urls import reverse
from .forms import Q_AForm, Q_A_AnswerForm
import mimetypes
from mimetypes import guess_type
import os
import re
from django.http import HttpResponse, HttpResponseRedirect, Http404
from urllib.parse import quote
import urllib
from django.conf import settings
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# 자유게시판 모두보기
class AllListView(ListView):
    model = Q_A
    paginate_by = 15
    template_name = 'Q_A/free_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'free_list'        #DEFAULT : <app_label>_list

    def get_queryset(self):
        free_list = Q_A.objects.order_by('-id') 

        return free_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
         
        return context



# 자유게시판 글 상세보기

def free_detail_view(request, pk):
    free = get_object_or_404(Q_A, pk=pk)
    comment = Q_A_Answer.objects.filter(board_id=pk).order_by('id')
    # comment_count = comment.count()
    # comment_count = comment.exclude(deleted=True).count()
    # reply = comment.exclude(reply='0')

    if request.user == free.writer:
        free_auth = True
    else:
        free_auth = False

    context = {
        'free': free,
        'free_auth': free_auth,
        'comments': comment,
        # 'comment_count': comment_count,
        # 'replys': reply,
    }
    response = render(request, 'Q_A/free_detail.html', context)
    free.hits += 1
    free.save()
    return response


# 자유게시판 글 쓰기
@login_required(login_url='common:login')
def free_write_view(request):
    if request.method == "POST":
        form = Q_AForm(request.POST, request.FILES)
        user_id = request.user
        
        if form.is_valid():
            free = form.save(commit = False)
            free.writer = user_id

            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    free.filename = request.FILES['upload_files'].name
                    
            free.save()
            return redirect('Q_A:all_list')
    else:
        form = Q_AForm()
    return render(request, "Q_A/free_write.html", {'form': form})


# 자유게시판 글 수정
@login_required(login_url='common:login')
def free_edit_view(request, pk):
    free = Q_A.objects.get(id=pk)
    if request.method == "POST":
        if(free.writer == request.user.username or request.user.username == 'admin' or request.user.username == 'cemuos'):

            file_change_check = request.POST.get('fileChange', False)
            file_check = request.POST.get('upload_files-clear', False)

            if file_check or file_change_check:
                os.remove(os.path.join(settings.MEDIA_ROOT, free.upload_files.path))

            form = Q_AForm(request.POST, request.FILES, instance=free)
            if form.is_valid():
                free = form.save(commit = False)

                if request.FILES:
                    if 'upload_files' in request.FILES.keys():
                        free.filename = request.FILES['upload_files'].name

                free.save()
                messages.success(request, "수정되었습니다.")
                return redirect('/Q_A/'+str(pk))
    else:
        free = Q_A.objects.get(id=pk)
        if free.writer == request.user.username or request.user.username == 'admin' or request.user.username == 'cemuos':
            form = Q_AForm(instance=free)
            context = {
                'form': form,
                'edit': '수정하기',
            }
            if free.filename and free.upload_files:
                context['filename'] = free.filename
                context['file_url'] = free.upload_files.url
            return render(request, "Q_A/free_write.html", context)
            # return render(request, "free/free_write.html", {'form': form, 'edit': '수정하기'})
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/Q_A/'+str(pk))


# 자유게시판 글 삭제
@login_required(login_url='common:login')
def free_delete_view(request, pk):
    free = Q_A.objects.get(id=pk)
    if free.writer == request.user.username or request.user.username == 'admin' or request.user.username == 'cemuos':
        free.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/Q_A/')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/Q_A/'+str(pk))


# 자유게시판 게시글 첨부파일 다운로드
@login_required(login_url='common:login')
def free_download_view(request, pk):
    free = get_object_or_404(Q_A, pk=pk)
    url = free.upload_files.url[1:]
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(free.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404


# # 게시글 댓글달기
# @login_required(login_url='common:login')
# def comment_write_view(request, pk):
#     post = get_object_or_404(Q_A, id=pk)
#     writer = request.POST.get('writer')
#     content = request.POST.get('content')
#     reply = request.POST.get('reply')
#     if content:
#         comment = Answer.objects.create(post=post, content=content, writer=request.user, reply=reply)
#         # comment_count = Comment.objects.filter(post=pk).count()
#         comment_count = Answer.objects.filter(post=pk).exclude(deleted=True).count()
#         post.comments = comment_count
#         post.save()
#         data = {
#             'writer': writer,
#             'content': content,
#             'created': '방금 전',
#             'comment_count': comment_count,
#             'comment_id': comment.id
#         }
#         if request.user == post.writer:
#             data['self_comment'] = '(글쓴이)'
        
#         return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")


# # 게시글 댓글 삭제
# @login_required(login_url='common:login')
# def comment_delete_view(request, pk):
#     post = get_object_or_404(Q_A, id=pk)
#     comment_id = request.POST.get('comment_id')
#     target_comment = Answer.objects.get(pk = comment_id)

#     if request.user.username == target_comment.writer or request.user.username == 'cmeuos' or request.user.username == 'admin':
#         # target_comment.delete()
#         # target_comment.content = ('삭제된 댓글입니다.')
#         target_comment.deleted = True
#         target_comment.save()
#         # comment_count = Comment.objects.filter(post=pk).count()
#         comment_count = Answer.objects.filter(post=pk).exclude(deleted=True).count()
#         post.comments = comment_count
#         post.save()
#         data = {
#             'comment_id': comment_id,
#             'comment_count': comment_count,
#         }
#         return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")

# @login_required(login_url='common:login')
# def answer_create(request, pk):
#     """
#     Q_A 답변등록
#     """
#     question = get_object_or_404(Q_A, pk=pk)
#     if request.method == "POST":
#         form = Q_A_AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user  # 추가한 속성 author 적용
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('/Q_A/'+str(pk))
#     else:
#         form = Q_A_AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'Q_A/free_detail.html', context)


# @login_required(login_url='common:login')
# def answer_modify(request, pk):
#     """
#     Q_A 답변수정
#     """
#     answer = get_object_or_404(Answer, pk=pk)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('Q_A:detail', question_id=answer.question.id)

#     if request.method == "POST":
#         form = Q_A_AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('/Q_A/'+str(pk))
#     else:
#         form = Q_A_AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'Q_A/answer_form.html', context)


# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     """
#     Q_A 답변삭제
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('/Q_A/'+str(pk))

def comment_create(request, pk):
    # 댓글 생성하는 로직
    content = request.POST.get('content')
    comment = Q_A_Answer()
    comment.board_id = pk
    comment.content = content
    comment.save()

    return redirect('Q_A:free_detail', pk)

def comment_delete(request, pk, comment_id):
    # 댓글 삭제 로직
    comment = Q_A_Answer.objects.get(pk=comment_id)
    comment.delete()

    return redirect('Q_A:free_detail', pk)