from api.generals.constants import MANDATORY_FIELDS_TO_EXCLUDE
from rest_framework import serializers


class AuraTestModelSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = MANDATORY_FIELDS_TO_EXCLUDE
        allow_empty = False
