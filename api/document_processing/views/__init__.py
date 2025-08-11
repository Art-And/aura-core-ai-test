from api.document_processing.views.classify_documents import ClassifyDocumentsViewSet
from api.document_processing.views.generate_signed_urls import GenerateSignedUrlView
from api.document_processing.views.upload_documents import UploadDocumentsViewSet


__all__ = [
    "GenerateSignedUrlView",
    "UploadDocumentsViewSet",
    "ClassifyDocumentsViewSet",
]
