import os
from django.db import models
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from uuid import uuid4
from django.contrib.auth.models import User

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    # return '/'.join(['upload_file/', ymd_path, uuid_name + extension,])
    return '/'.join(['member_board_Phd/', ymd_path, uuid_name+extension])

# Create your models here.
class member_post_MA(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True, verbose_name = '제목')
    content = models.TextField(blank=True)
    email = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=timezone.now)
    photo = models.ImageField(upload_to = 'media/member_board_MA',blank = True, null=True)

    def __str__(self):
        return self.title
     
    def delete(self, *args, **kargs):
        if self.photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(member_post_MA, self).delete(*args, **kargs)
    
    class Meta:
        db_table = 'member_board_MA'
        verbose_name = 'member_board_MA'
        verbose_name_plural = 'member_board_MA'