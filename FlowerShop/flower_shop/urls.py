from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^services/', views.services, name='services'),
    url(r'^shop/', views.shop, name='shop'),
    url(r'^portfolio/', views.portfolio, name='portfolio'),
]
