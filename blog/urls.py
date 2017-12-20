__author__ = 'xue'
__date__ = '2017/12/19 22:23'
from django.conf.urls import url

from .views import  post_detail, PostListView



urlpatterns = [
    # url(r'^$', post_list, name='post_list'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', post_detail, name='post_detail'),
]