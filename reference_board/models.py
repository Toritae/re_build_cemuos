from django.db import models
from django.conf import settings
# Create your models here.
class DataRoom(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='media/reference_room')
    
    class Meta:
        db_table = 'DataRoom'
        verbose_name = 'DataRoom'
        verbose_name_plural = 'DataRoom'