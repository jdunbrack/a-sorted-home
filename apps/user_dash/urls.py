from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.base_redir),
    url(r'^dash$', views.index),
    url(r'^dash/edit$', views.edit_user),
    url(r'^update$', views.update_user),
    url(r'^check-pw$', views.pw_verify),
    url(r'^validate-pw$', views.pw_validate),
    url(r'^change-pw$', views.pw_update),
    url(r'^dash/edit-payment$', views.edit_payment),
    url(r'^home/create$', views.create_home),
    url(r'^home/join$', views.join_home),
    url(r'^home/leave$', views.leave_home),
    url(r'^home/delete$', views.delete_home),
    url(r'^home/edit$', views.edit_home),
    url(r'^home/remove/(?P<user_id>\d+)$', views.remove_member),
    url(r'^add-picture$', views.upload_image),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
