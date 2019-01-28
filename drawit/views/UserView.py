from drawit.models import *
from drawit.serializers import *
from rest_framework import generics

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
