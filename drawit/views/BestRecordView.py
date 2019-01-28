from django.shortcuts import get_object_or_404
from drawit.models import *
from drawit.serializers import *
from rest_framework import generics

class BestRecordCreateView(generics.ListCreateAPIView):
    serializer_class = BestRecordSerializer
    
    def get_queryset(self):
       stage_id = self.kwargs['stage_id']
       return BestRecord.objects.filter(stage_id=stage_id)

class BestRecordUpdateView(generics.RetrieveUpdateDestroyAPIView):
	queryset = BestRecord.objects.all()
	serializer_class = BestRecordSerializer

	def get_object(self):
		queryset = self.filter_queryset(self.get_queryset())
		stage_id = self.kwargs['stage_id']
		user_id = self.kwargs['user_id']

		obj = get_object_or_404(BestRecord, stage_id=stage_id, user_id=user_id)
		
		self.check_object_permissions(self.request, obj)
		return obj

