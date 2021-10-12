import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from uuid import uuid4
from notice.models import get_file_path


class Q_A(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='이미지파일') # summernote MultiValueDict : files
    upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')

    def __str__(self):
        return self.title

    # def filename(self):
    #     return os.path.basename(self.upload_files.name)

    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(QA, self).delete(*args, **kargs)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.registered_date

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
            return str(time.days) + '일 전'
        else:
            return False

    class Meta:
        db_table = 'Q_A'
        verbose_name = 'Q_A'
        verbose_name_plural = 'Q_A'


class Q_A_Answer(models.Model):
    # author =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_answer',blank=True)
    # question = models.ForeignKey(QA, on_delete=models.CASCADE,blank=True)
    # content = models.TextField(blank=True)
    # create_date = models.DateTimeField(blank=True)
    # modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)  # auto_now_add : '객체를 하나 생성할 때만 시간을 담겠다' 라는 의미
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)  # auto_now : 지금 작업을 할 때
    # 일(게시판) 대 다(댓글들) 관계 이기 때문에 foreign key 설정을 해줘야한다.
    board = models.ForeignKey(QA, on_delete=models.CASCADE,blank=True)

    class Meta:
        db_table = 'Q_A_Answer'
        verbose_name = 'Q_A_Answer'
        verbose_name_plural = 'Q_A_Answer'