from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^game/$', views.my_game, name='my_game'),
    url(r'^clock/$', views.clock, name='clock'),
    url(r'^image/$', views.image, name='image'),
]