from rest_framework import serializers

class AnalysisSerializer(serializers.Serializer):
    description = serializers.CharField() 

