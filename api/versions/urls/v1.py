from django.urls import path, include

urlpatterns = [
    path("v1/", include("document_processing.urls"))
]