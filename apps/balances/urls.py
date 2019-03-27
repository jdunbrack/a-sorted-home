from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.post),
    url(r'^query/(?P<user_id>\d+)$', views.get_transactions),
    url(r'^clear/(?P<user_id>\d+)$', views.all_paid),
    url(r'^remove/(?P<txn_id>\d+)$', views.remove_txn),
]