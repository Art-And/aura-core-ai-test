from django.contrib.postgres.fields import ArrayField
from django.db import models
from generals.abstract_models import BaseAbstractModel
from generals.constants import FileTypes


class Document(BaseAbstractModel):
    name = models.TextField(max_length=250)
    file_type = models.TextField(choices=FileTypes)
    content = models.TextField()
    embedding = ArrayField(models.FloatField(), null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.file_type})"

    class Meta(BaseAbstractModel.Meta):
        verbose_name_plural = "Documents"
        app_label = "document_processing"
