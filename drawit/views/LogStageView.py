from drawit.models import *
from drawit.serializers import *
from rest_framework import generics

class LogStageCreateView(generics.ListCreateAPIView):
    queryset = LogStage.objects.all()
    serializer_class = LogStageCreateSerializer

class LogStageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogStage.objects.all()
    serializer_class = LogStageUpdateSerializer

class LogStageInfoListView(generics.ListAPIView):
    queryset = LogStage.objects.all()
    serializer_class = LogStageInfoSerializer