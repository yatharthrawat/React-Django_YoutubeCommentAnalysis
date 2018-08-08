from rest_framework import serializers

class AnalysisSerializer(serializers.Serializer):
    author = serializers.CharField()
    text = serializers.CharField()
    sentiment = serializers.CharField()

