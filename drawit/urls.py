from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from drawit.views import *

urlpatterns = [
    url(r'^stage/$', LogStageCreateView.as_view()),
    url(r'^stage/(?P<pk>[a-z0-9]+)/$', LogStageUpdateView.as_view()),
    url(r'^stage_info/$', LogStageInfoListView.as_view()),
    url(r'^user/$', UserCreateView.as_view()),
    url(r'^bestrecord/(?P<stage_id>[0-9]+)/$', BestRecordCreateView.as_view()),
    url(r'^bestrecord/(?P<stage_id>[0-9]+)/(?P<user_id>.+)/$', BestRecordUpdateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
