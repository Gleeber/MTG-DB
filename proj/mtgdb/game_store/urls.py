from django.conf.urls import url
from . import views

app_name = 'game_store'

urlpatterns = [
    url(r'^$',views.game_store_list, name='list'),
    url(r'^(?P<id>[0-9]+)/$', views.game_store_info, name='info')
]
