from rest_framework import serializers
from drawit.models.User import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
