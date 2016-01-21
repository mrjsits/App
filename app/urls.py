from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^service/$', views.serviceview, name = 'serviceview'),
	url(r'^home/$', views.home, name = 'home'),
	url(r'^$', views.home, name = 'home'),
	url(r'^register/$', views.register, name = 'register'),
	url(r'^login/$',views.loginview, name = 'loginview'),
	url(r'^logout/$', views.logoutview, name = 'logoutview'),
]