from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'KittyWar/register/$', views.registration, name = 'registration'),
    url(r'KittyWar/login/$', views.login, name = 'login')
]


