from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'card'

urlpatterns = [
    url(r'^$',views.card_list, name='list')
]
