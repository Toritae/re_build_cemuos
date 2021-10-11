from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class seminar_post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True,null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목',blank=True)
    content = models.TextField(verbose_name='내용',blank=True)
    create_date = models.DateTimeField(default=timezone.now,blank=True)
    upload_files = models.FileField(upload_to='media/seminar/',null=True,blank=True)
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명',blank=True)
    
    class Meta:
        db_table = 'seminar'
        verbose_name = 'seminar'
        verbose_name_plural = 'seminar'