from django.urls import include, path

from api.document_processing.views import (
    ClassifyDocumentsViewSet,
    GenerateSignedUrlView,
    UploadDocumentsViewSet,
)


urlpatterns = [
    path(
        "generate-signed-url/",
        GenerateSignedUrlView.as_view(),
        name="generate-signed-url",
    ),
    path(
        "upload-documents/",
        UploadDocumentsViewSet.as_view({"post": "create"}),
        name="upload-document",
    ),
    path(
        "classify-documents/",
        ClassifyDocumentsViewSet.as_view({"post": "create"}),
        name="classify-document",
    ),
]
