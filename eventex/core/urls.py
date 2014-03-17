# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import HomeView, SpeakerDetail

urlpatterns = patterns('eventex.core.views',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetail.as_view(), name='speaker_detail'),
    url(r'^palestras/$', 'talk_list', name='talk_list'),
    url(r'^palestras/(?P<pk>\d+)/$', 'talk_detail', name='talk_detail'),
)