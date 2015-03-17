from django.conf.urls import include, patterns, url

from . import views

urlpatterns = patterns(
    'madness',
    url(r'^bracket/create/$', views.CreateEntryView.as_view(), name='create_entry'),
    url(r'^bracket/create/(?P<pk>\d+)/$', views.EnterPicksView.as_view(), name='entry_picks'),
)
