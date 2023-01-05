from rest_framework import serializers

from .models import DummyData

class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyData
        fields = '__all__'
