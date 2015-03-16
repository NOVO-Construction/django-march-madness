from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns(
    'madness',
    url(r'^bracket/$', views.EntryPicks, name='entry_picks'),
)