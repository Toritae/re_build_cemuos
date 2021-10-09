from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class DataRoom(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목',blank=True)
    content = models.TextField(verbose_name='내용',blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    upload_files = models.FileField(upload_to='media/reference_room/',null=True,blank=True)
    
    class Meta:
        db_table = 'DataRoom'
        verbose_name = 'DataRoom'
        verbose_name_plural = 'DataRoom'