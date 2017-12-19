# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=250)),
                ('slug', models.SlugField(verbose_name='标签', max_length=250, unique_for_date='publish')),
                ('body', models.TextField(verbose_name='内容')),
                ('publish', models.DateTimeField(verbose_name='发布时间', default=django.utils.timezone.now)),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('status', models.CharField(verbose_name='文章状态', max_length=10, default='draft', choices=[('draft', '草稿'), ('published', '已发布的')])),
                ('author', models.ForeignKey(verbose_name='作者', related_name='blog_posts', on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ('-publish',),
            },
        ),
    ]
