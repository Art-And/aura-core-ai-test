from django.urls import include, path
from api.document_processing.views import GenerateSignedUrlView

urlpatterns = [
    path("generate-signed-url/", GenerateSignedUrlView.as_view(), name="generate-signed-url"),
]
