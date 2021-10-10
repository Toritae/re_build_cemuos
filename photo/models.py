import os
from django.db import models
from django.utils import timezone
from django.conf import settings
from datetime import datetime
from uuid import uuid4
from django.contrib.auth.models import User


# Create your models here.
class photo_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True, verbose_name = '제목')
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=timezone.now)
    photo = models.ImageField(upload_to = 'media/photo/',blank = True, null=True)

    def __str__(self):
        return self.title
     
    def delete(self, *args, **kargs):
        if self.photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(photo_post, self).delete(*args, **kargs)
    
    class Meta:
        db_table = 'photo'
        verbose_name = 'photo'
        verbose_name_plural = 'photo'