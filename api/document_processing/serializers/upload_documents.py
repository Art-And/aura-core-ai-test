from document_processing.models import Document
from rest_framework import serializers


class UploadDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "id",
            "name",
            "file_type",
            "content",
            "embedding",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
