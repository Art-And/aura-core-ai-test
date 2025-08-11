from api.core.settings.base import *
from google.oauth2 import service_account

STORAGES["staticfiles"] = {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    }
STORAGES["default"] = {
    "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
}
GS_BUCKET_NAME = 'aura-core-ai-test'
GS_CREDENTIALS = (
    service_account.Credentials.from_service_account_file(
        f"{BASE_DIR.parent}/aura_test_credentials.json"
    )
)
