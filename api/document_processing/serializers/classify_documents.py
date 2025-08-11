from document_processing.models import DocumentClassification
from rest_framework import serializers


class ClassifyDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentClassification
        fields = [
            "id",
            "document",
            "confidence_score",
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
