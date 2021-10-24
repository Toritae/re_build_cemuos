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
    return ''.join(['media/property_3/', uuid_name+extension])
# Create your models here.
class property_3(models.Model):
    pid = models.CharField(max_length=128, verbose_name='번호',blank=True)
    content = models.TextField(verbose_name='내용',blank=True)
    content_created = models.CharField(max_length=128, verbose_name='등록일자',blank=True)
    create_date = models.DateTimeField(default=timezone.now,blank=True)
    upload_files = models.FileField(upload_to=get_file_path,null=True,blank=True)
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명',blank=True)
    
    class Meta:
        db_table = 'property_3'
        verbose_name = 'property_3'
        verbose_name_plural = 'property_3'