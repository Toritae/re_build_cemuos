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
    class Meta:
        db_table = 'sitelink_1'
        verbose_name = 'sitelink_1'
        verbose_name_plural = 'sitelink_1'

class Sitelink_2(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='sitelink')
    create_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'sitelink_2'
        verbose_name = 'sitelink_2'
        verbose_name_plural = 'sitelink_2'

class Sitelink_3(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='sitelink')
    create_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'sitelink_3'
        verbose_name = 'sitelink_3'
        verbose_name_plural = 'sitelink_3'
        
class Sitelink_4(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='sitelink')
    create_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'sitelink_4'
        verbose_name = 'sitelink_4'
        verbose_name_plural = 'sitelink_4'

class Sitelink_5(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='sitelink')
    create_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'sitelink_5'
        verbose_name = 'sitelink_5'
        verbose_name_plural = 'sitelink_5'
        
class Sitelink_6(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='sitelink')
    create_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'sitelink_6'
        verbose_name = 'sitelink_6'
        verbose_name_plural = 'sitelink_6'