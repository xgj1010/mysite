# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='标题')),
                ('slug', models.SlugField(max_length=250, verbose_name='标签', unique_for_date='publish')),
                ('body', models.TextField(verbose_name='内容')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '已发布的')], default='draft', max_length=10, verbose_name='文章状态')),
                ('author', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL, related_name='blog_posts', on_delete=True)),
            ],
            options={
                'ordering': ('-publish',),
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
