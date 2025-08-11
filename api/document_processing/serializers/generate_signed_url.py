from rest_framework import serializers

class GenerateSignedUrlSerializer(serializers.Serializer):
    file_name = serializers.CharField(max_length=100)
    content_type = serializers.CharField(max_length=100)
