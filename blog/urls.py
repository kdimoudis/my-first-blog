from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_start, name='post_start'),
    url(r'^review/$', views.post_list, name='post_list'),
    url(r'^review/label/$', views.post_list2, name='post_list2'),
    url(r'^review/composer/$', views.post_list3, name='post_list3'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
