from rest_framework import serializers
from cms.models import ProtectionLevel, TrendQuery


class ProetctionLevelSerializer(serializers.Serializer):
    class Meta:
        model = ProtectionLevel
        fields = ('__all__')
    
    def create(self, validated_data):
        return ProtectionLevel(**validated_data)


class TrendQuerySerializer(serializers.Serializer):
    class Meta:
        model = TrendQuery
        fields = ('__all__')

