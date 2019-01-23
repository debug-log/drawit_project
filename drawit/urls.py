from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from drawit.views import *

urlpatterns = [
    url(r'^stage/$', LogStageCreate.as_view()),
    url(r'^stage/(?P<pk>[a-z0-9]+)/$', LogStageUpdate.as_view()),
    url(r'^stage_info/$', LogStageInfoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
