from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^assign$', views.assign),
    url(r'^finish$', views.finish),
    url(r'^info/(?P<task_id>\d+)$', views.get_info),
]