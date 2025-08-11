from django.urls import include, path
from api.document_processing.views import GenerateSignedUrlView,UploadDocumentsViewSet

urlpatterns = [
    path("generate-signed-url/", GenerateSignedUrlView.as_view(), name="generate-signed-url"),
    path("upload-document/", UploadDocumentsViewSet.as_view({"post": "create"}), name="upload-document"),
]
