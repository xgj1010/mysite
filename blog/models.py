from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """文章"""
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '已发布的'),
    )
    title = models.CharField(max_length=250, verbose_name='标题')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='标签')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=True, verbose_name='作者')
    body = models.TextField(verbose_name='内容')
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='文章状态')

    class Meta:
        ordering = ('-publish',)
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse(
            'blog:post_detail', args=[
                self.publish.year,
                self.publish.strftime('%m'),
                self.publish.strftime('%d'),
                self.slug
            ]
        )
    tags = TaggableManager()


class Comment(models.Model):
    """评论"""
    post = models.ForeignKey(Post, related_name='comments', verbose_name='文章')
    name = models.CharField(max_length=80, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    body = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateField(auto_now=True, verbose_name='更新时间')
    active = models.BooleanField(default=True, verbose_name='是否激活')

    class Meta:
        ordering = ('created',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
