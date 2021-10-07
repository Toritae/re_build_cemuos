# Generated by Django 3.2.7 on 2021-10-07 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import member_board_alum_MA_city.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='member_post_alum_MA_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='제목')),
                ('content', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=member_board_alum_MA_city.models.get_file_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'member_board_alum_MA_city',
                'verbose_name_plural': 'member_board_alum_MA_city',
                'db_table': 'member_board_alum_MA_city',
            },
        ),
    ]
