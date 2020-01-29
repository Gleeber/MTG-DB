from django.conf.urls import url
from . import views

app_name = 'event'

urlpatterns = [
    url(r'^$',views.event_list, name='list'),
    url(r'^(?P<id>[0-9]+)/$', views.event_info, name='info')
]
