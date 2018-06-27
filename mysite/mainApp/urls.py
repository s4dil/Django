from django.urls import path, re_path, include
from . import views

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^contact/$', views.contact, name='contact'),
]