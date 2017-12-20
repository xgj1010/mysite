# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',), 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True, verbose_name='是否激活'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(verbose_name='邮箱', max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(verbose_name='姓名', max_length=80),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', verbose_name='文章', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateField(verbose_name='更新时间', auto_now=True),
        ),
    ]
