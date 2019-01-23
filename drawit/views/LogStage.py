from drawit.models import *
from drawit.serializers import *
from rest_framework import generics

class LogStageCreate(generics.ListCreateAPIView):
    queryset = LogStage.objects.all()
    serializer_class = LogStageCreateSerializer

class LogStageUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogStage.objects.all()
    serializer_class = LogStageUpdateSerializer

class LogStageInfoList(generics.ListAPIView):
    queryset = LogStage.objects.all()
    serializer_class = LogStageInfoSerializer