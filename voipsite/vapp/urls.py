"""voipproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from .views import UpdateRules

urlpatterns = [
	url(r'^$', views.index, name= 'list'),
	url(r'^create/$', views.post_create),
	url(r'^(?P<id>\d+)/sound_detail/$', views.sound_detail),
	url(r'^createnum/$', views.post_createnum),
	url(r'^update_rules/(?P<pk>[\w-]+)$', UpdateRules.as_view(), name='update_rules'),
	url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
	url(r'^(?P<id>\d+)/delete/$', views.post_delete, name= 'delete'),
]
