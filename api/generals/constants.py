from django.db.models import Choices


class BoolChoices(Choices):
    YES: bool = True
    NO: bool = False


MANDATORY_FIELDS_TO_EXCLUDE = [
    "created_at",
    "updated_at",
]
