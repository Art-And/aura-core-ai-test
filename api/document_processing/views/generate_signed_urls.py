from document_processing.services import GCPCloudStorageService
from generals import StorageConstants
from google.api_core.exceptions import Forbidden, GoogleAPIError, NotFound
from google.auth.exceptions import GoogleAuthError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.document_processing.serializers import GenerateSignedUrlSerializer


class GenerateSignedUrlView(APIView):
    serializer_class = GenerateSignedUrlSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": "Invalid parameters provided.", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        file_name = serializer.data.get("file_name")
        content_type = serializer.data.get("content_type")
        bucket_name = str(StorageConstants.Buckets.TEMPORAL.value)
        bucket_path = str(StorageConstants.Paths.TEMPORAL_DOCUMENT.value)
        try:
            (
                signed_url,
                file_name_identifier,
            ) = GCPCloudStorageService().generate_signed_url(
                file_name=file_name,
                bucket_name=bucket_name,
                bucket_path=bucket_path,
                content_type=content_type,
            )
            return Response(
                data={"file_name": file_name_identifier, "url": signed_url},
                status=status.HTTP_201_CREATED,
            )
        except NotFound as e:
            return Response(
                {
                    "error": f"The specified bucket {bucket_name} was not found.",
                    "details": str(e),
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Forbidden as e:
            return Response(
                {
                    "error": f"Access denied to bucket {bucket_name}. Check your permissions.",
                    "details": str(e),
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        except GoogleAuthError as e:
            return Response(
                {
                    "error": "There was an authentication error. Check your GCP credentials.",
                    "details": str(e),
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except ValueError as e:
            return Response(
                {"error": "Invalid parameter provided.", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except GoogleAPIError as e:
            return Response(
                {"error": "An error occurred with the Google API.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
