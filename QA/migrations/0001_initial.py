# Generated by Django 3.2.8 on 2021-10-11 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import notice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('comments', models.PositiveIntegerField(null=True, verbose_name='댓글수')),
                ('files', models.FileField(blank=True, null=True, upload_to=notice.models.get_file_path, verbose_name='이미지파일')),
                ('upload_files', models.FileField(blank=True, null=True, upload_to=notice.models.get_file_path, verbose_name='파일')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': 'QA',
                'verbose_name_plural': 'QA',
                'db_table': 'QA',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='댓글내용')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('reply', models.IntegerField(default=0, verbose_name='답글위치')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QA.qa', verbose_name='게시글')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='댓글작성자')),
            ],
            options={
                'verbose_name': 'QA_Answer',
                'verbose_name_plural': 'QA_Answer',
                'db_table': 'QA_Answer',
            },
        ),
    ]