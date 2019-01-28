from rest_framework import serializers
from drawit.models.BestRecord import BestRecord

class BestRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestRecord
        fields = ('stage_id', 'user', 'record',)

    def create(self, validated_data):
        return BestRecord.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.stage_id = validated_data.get('stage_id', instance.stage_id)
        instance.user = validated_data.get('user', instance.user)
        instance.record = validated_data.get('record', instance.record)
        instance.save()
        return instance

