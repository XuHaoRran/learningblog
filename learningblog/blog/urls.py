from django.conf.urls import url
from . import views


app_name='blog'
urlpatterns=[
    #第一个是网址，第二个参数是处理函数，第三个是作为处理函数index的别名
    url(r'^$',views.index,name='index'),
    url(r'^post/$',views.detail),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
]