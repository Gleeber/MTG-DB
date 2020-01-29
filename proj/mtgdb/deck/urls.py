from django.conf.urls import url
from . import views

app_name = 'deck'

urlpatterns = [
    url(r'^$',views.deck_list, name='list'),
    url(r'^(?P<id>[0-9]+)/$', views.deck_info, name='info')
]
