from django.conf.urls import patterns, include, url

from weixin.views import *

# urlpatterns=patterns('',
#     url(r'^$','weixin.views.Index'),
#
# )

# urlpatterns = [
#    url(r'^weixin/', IndexView.as_view()),
#    # url(r'weixin/main^$', IndexView.as_view()),
# ]

urlpatterns=patterns('',
    url(r'^weixin/$','weixin.views.Index'),
    url(r'^test/$', IndexView.as_view()),
)