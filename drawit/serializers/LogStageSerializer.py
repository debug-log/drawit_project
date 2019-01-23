from rest_framework import serializers
from drawit.models.LogStage import LogStage

class LogStageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogStage
        fields = ('stage_id',)

    def create(self, validated_data):
        return LogStage.objects.create(**validated_data)

class LogStageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogStage
        fields = ('stage_id', 'types')

    def update(self, instance, validated_data):
        instance.stage_id = validated_data.get('stage_id', instance.stage_id)
        instance.types = validated_data.get('types', instance.types)

        if instance.types == 'success':
            instance.success_count += 1
        elif instance.types == 'star0':
            instance.star0_count += 1
        elif instance.types == 'star1':
            instance.star1_count += 1
        elif instance.types == 'star2':
            instance.star2_count += 1

        instance.try_count += 1
        instance.save()
        return instance

class LogStageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogStage
        fields = ('stage_id', 'try_count', 'success_count', 'star0_count', 'star1_count', 'star2_count')

    def create(self, validated_data):
        return LogStage.objects.create(**validated_data)