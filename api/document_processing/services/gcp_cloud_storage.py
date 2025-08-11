import uuid
from datetime import timedelta
from google.cloud import storage
from generals import StorageConstants
from django.conf import settings


class GCPCloudStorageService:

    @staticmethod
    def generate_uuid_file_name(file_name: str) -> str:
        random_uuid = uuid.uuid4()
        return f"{random_uuid}_{file_name}"

    def generate_full_path(self, bucket_path: str, file_name: str) -> tuple[str, str]:
        """
        Generates a full file path by combining the provided bucket path with a
        generated unique file name. Returns the full path and the unique file
        name as a tuple.

        :param bucket_path: Path to the bucket where the file should be stored.
        :type bucket_path: str
        :param file_name: Original name of the file that will be used to generate
            a unique identifier.
        :type file_name: str
        :return: A tuple containing the full path to the file and the unique file
            name.
        :rtype: tuple[str, str]
        """
        file_name_identifier = self.generate_uuid_file_name(file_name)
        return (
            f"{bucket_path}/{file_name_identifier}",
            file_name_identifier,
        )

    def generate_signed_url(
            self,
            file_name: str,
            bucket_name: str,
            bucket_path: str,
            content_type: str,
            expiration_minutes: int = StorageConstants.LifeTime.DEFAULT.value,
    ) -> tuple[str, str]:
        """
        Generate a signed URL to upload a file to a GCP bucket.

        :param file_name: Name of the file to be uploaded (includes prefix if necessary).
        :param bucket_name: Name of the bucket where the file will be uploaded.
        :param bucket_path: Name of the path in the bucket where the file will be uploaded.
        :param content_type: Type of the file to be uploaded.
        :param expiration_minutes: Lifetime of the signed URL in minutes (default is 15 minutes).
        :return: Signed URL for uploading the file.
        """

        client = storage.Client(credentials=settings.GS_CREDENTIALS)
        full_path, file_name_identifier = self.generate_full_path(bucket_path, file_name)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(full_path)

        url = blob.generate_signed_url(
            version="v4",
            expiration=timedelta(minutes=expiration_minutes),
            method="PUT",
            content_type=content_type,
        )
        return url, file_name_identifier