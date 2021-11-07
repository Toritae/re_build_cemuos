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
    return ''.join(['media/professor_hyun_4/', uuid_name+extension])
# Create your models here.
class professor_hyun_4(models.Model):
    pid = models.TextField(verbose_name='번호',blank=True)
    content = models.TextField(verbose_name='내용',blank=True)
    create_date = models.DateTimeField(default=timezone.now,blank=True)
    
    class Meta:
        db_table = 'professor_hyun_4'
        verbose_name = 'professor_hyun_4'
        verbose_name_plural = 'professor_hyun_4'