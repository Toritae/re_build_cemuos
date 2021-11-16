import os
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from uuid import uuid4
from notice.models import get_file_path


class Sitelink(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='sitelink')
    create_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title

    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Sitelink, self).delete(*args, **kargs)
