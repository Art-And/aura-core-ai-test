from django.db.models import Choices
from django.db.models import TextChoices, IntegerChoices


class BoolChoices(Choices):
    YES: bool = True
    NO: bool = False


MANDATORY_FIELDS_TO_EXCLUDE = [
    "created_at",
    "updated_at",
]

class StorageConstants:
    class Buckets(TextChoices):
        TEMPORAL = "temporal-aura-core-ai-test",  "Temporal Files"
        PERMANENT = "aura-core-ai-test", "Permanent Files"

    class Paths(TextChoices):
        TEMPORAL_DOCUMENT = "documents", "Temporal Document"
        PERMANENT_DOCUMENT = "accounts/documents", "Permanent Document"

    class LifeTime(IntegerChoices):
        DEFAULT = 15, "Default Lifetime (minutes)"
        ONE_DAY = 720, "One Day Lifetime (minutes)"
