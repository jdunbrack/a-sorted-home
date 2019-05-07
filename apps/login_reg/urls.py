from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing),
    url(r'check-email$', views.email_verify),
    url(r'check-pw$', views.pw_verify),
    url(r'register$', views.add_user),
    url(r'logout$', views.logout),
    url(r'check-name$', views.name_verify),
]
