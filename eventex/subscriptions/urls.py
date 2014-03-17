# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import SubscriptionDetail

urlpatterns = patterns('eventex.subscriptions.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(?P<pk>\d+)/$', SubscriptionDetail.as_view(), name='detail'),
)