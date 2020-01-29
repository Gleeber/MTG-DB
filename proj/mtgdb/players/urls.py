from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'players'

urlpatterns = [
    url(r'^$',views.player_list, name='list')
]
