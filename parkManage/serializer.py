from rest_framework import serializers
from parkManage.models import *


class CarSerializer(serializers.ModelSerializer):
    duration_s = serializers.DurationField(source='duration', read_only=True)
    class Meta:
        model = Current_Car
        fields = ['brand','duration_s']
    def create(self,validated_data):
        return Current_Car.objects.create(**validated_data)

    def get(self, request):
        data = Current_Car.objects.all()

