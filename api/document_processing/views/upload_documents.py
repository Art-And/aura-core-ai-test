from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from rest_framework.response import Response
from api.document_processing.models import Document
from generals.pagination import AuraTestPagination
from rest_framework import serializers
from api.document_processing.services import EmbeddingsService, GCPCloudStorageService, ReadDocumentsService
from generals import StorageConstants
from google.api_core.exceptions import NotFound, Forbidden
from google.auth.exceptions import GoogleAuthError


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


class UploadDocumentsViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = UploadDocumentsSerializer
    pagination_class = AuraTestPagination

    def modify_request_data(self, blob_file):
        file_name = self.request.data.pop("file_name")
        file_type = file_name.split('.')[-1].lower()
        text_content = ReadDocumentsService().get_content_from_file(blob_file)
        embedding_list = EmbeddingsService.generate_embedding(text_content)

        self.request.data.update(
            {
                "name": file_name,
                "file_type": file_type,
                "content": text_content,
                "embedding": embedding_list,
            }
        )

    def create(self, request, *args, **kwargs):
        if not (file_name := request.data.get("file_name", None)):
            return Response(
                {
                    "error": "No file name provided.",
                    "details": "Please provide a file name."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        source_blob_name = GCPCloudStorageService.get_path_with_name(
            StorageConstants.Paths.TEMPORAL_DOCUMENT,
            file_name
        )
        destination_blob_name = GCPCloudStorageService.get_path_with_name(
            StorageConstants.Paths.PERMANENT_DOCUMENT,
            file_name
        )

        try:
            blob_file = GCPCloudStorageService.copy_between_buckets(
                source_bucket_name=str(StorageConstants.Buckets.TEMPORAL.value),
                source_blob_name=source_blob_name,
                destination_bucket_name=str(StorageConstants.Buckets.PERMANENT.value),
                destination_blob_name=destination_blob_name,
            )

            self.modify_request_data(blob_file)
            return super().create(request, *args, **kwargs)

        except NotFound as e:
            return Response(
                {
                    "error": f"The file {file_name} was not found.",
                    "details": str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Forbidden as e:
            return Response({
                "error": f"Access denied to the bucket. Check your permissions.",
                "details": str(e)
            }, status=status.HTTP_403_FORBIDDEN)

        except GoogleAuthError as e:
            return Response({
                "error": "There was an authentication error. Check your GCP credentials.",
                "details": str(e)
            }, status=status.HTTP_401_UNAUTHORIZED)
