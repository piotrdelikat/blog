from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^privacy-policy/$', views.privacy, name='privacy'),
    url(r'^frankentie_promo/', views.promo, name='promo')
]

