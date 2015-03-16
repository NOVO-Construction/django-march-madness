# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djrill import urls as djrill_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^djrill/', include(djrill_urls)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^madness/', include('madness.urls', namespace='madness')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
