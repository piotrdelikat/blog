from django.conf.urls import url
from django.views.generic import DetailView
from .models import *
from . import views

app_name='blog'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail")
]

