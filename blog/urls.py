from django.conf.urls import url
from django.views.generic import DetailView
from .models import *
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model= Post, template_name="blog/post.html"))
]

