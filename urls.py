from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.musical_group, name='musical_group'),
url(r'^$', views.group_user, name='group_user')
]