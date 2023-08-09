from rest_framework import serializers

class SecurityLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()