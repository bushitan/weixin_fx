# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('blog.urls')),
    # url(r'', include('vmaig_comments.urls')),
    # url(r'', include('vmaig_auth.urls')),
    # url(r'', include('art.urls')),
    url(r'^weixin/', include('weixin.urls')),
    # url(r'', include('time_line.urls')),
]
