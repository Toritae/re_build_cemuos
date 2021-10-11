# Generated by Django 3.2.8 on 2021-10-11 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='제목')),
                ('content', models.TextField(blank=True, verbose_name='내용')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload_files', models.FileField(blank=True, null=True, upload_to='media/reference_room/')),
                ('filename', models.CharField(blank=True, max_length=64, null=True, verbose_name='첨부파일명')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': 'DataRoom',
                'verbose_name_plural': 'DataRoom',
                'db_table': 'DataRoom',
            },
        ),
    ]
