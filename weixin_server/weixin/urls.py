from django.conf.urls import patterns, include, url

from weixin.views import *

# urlpatterns=patterns('',
#     url(r'^$','weixin.views.Index'),
#
# )

urlpatterns = [
   url(r'^weixin/', IndexView.as_view()),
   # url(r'weixin/main^$', IndexView.as_view()),
]