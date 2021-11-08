from django.db import models
from django.conf import settings
from django.utils import timezone
from uuid import uuid4
import os

# Create your models here.
def get_file_path(instance, filename):
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    # return '/'.join(['upload_file/', ymd_path, uuid_name + extension,])
    return ''.join(['media/professor_lee_2/', uuid_name+extension])
# Create your models here.
class professor_lee_2(models.Model):
    pid = models.CharField(max_length=128, verbose_name='논문번호',blank=True)
    content = models.TextField(verbose_name='내용',blank=True)
    content_created = models.CharField(max_length=128, verbose_name='출판년월',blank=True)
    create_date = models.DateTimeField(default=timezone.now,blank=True)
    
    class Meta:
        db_table = 'professor_lee_2'
        verbose_name = 'professor_lee_2'
        verbose_name_plural = 'professor_lee_2'