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
    return 'media/'.join(['pj_board_gov/', ymd_path, uuid_name+extension])

# Create your models here.
class pj_post_gov(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True, verbose_name = '제목')
    content = models.TextField(blank=True)
    front_content = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=timezone.now)
    photo = models.ImageField(upload_to = get_file_path)

    def __str__(self):
        return self.title
     
    def delete(self, *args, **kargs):
        if self.photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(pj_post_gov, self).delete(*args, **kargs)
    
    class Meta:
        db_table = 'pj_board_gov'
        verbose_name = 'pj_board_gov'
        verbose_name_plural = 'pj_board_gov'