from generals import StorageConstants
from generals.pagination import AuraTestPagination
from google.api_core.exceptions import Forbidden, NotFound
from google.auth.exceptions import GoogleAuthError
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.document_processing.models import Document, DocumentClassification
from api.document_processing.serializers import ClassifyDocumentsSerializer
from api.document_processing.services import TextClassifier


class ClassifyDocumentsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = DocumentClassification.objects.all()
    serializer_class = ClassifyDocumentsSerializer
    pagination_class = AuraTestPagination

    def add_require_data(self, document_id: int):

        text_content = (
            Document.objects.filter(pk=document_id)
            .values_list("content", flat=True)
            .first()
        )

        if not text_content:
            return Response(
                {
                    "error": "The document was not found.",
                    "details": "Please check the document ID.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        category, confidence_score = TextClassifier.classify_document(text_content)
        self.request.data.update(
            {
                "category": category,
                "confidence_score": confidence_score,
            }
        )

    def create(self, request, *args, **kwargs):

        if not (document_id := request.data.get("document", None)):
            return Response(
                {
                    "error": "No document ID provided.",
                    "details": "Please provide a document ID.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.add_require_data(document_id)
        return super().create(request, *args, **kwargs)
