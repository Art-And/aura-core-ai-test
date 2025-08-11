from django.db import models

from api.generals.abstract_models import BaseAbstractModel


class DocumentClassification(BaseAbstractModel):
    document = models.ForeignKey(
        "document_processing.Document",
        on_delete=models.CASCADE,
        related_name="classifications",
    )
    category = models.TextField()
    confidence_score = models.FloatField()

    def __str__(self):
        return f"{self.category} ({self.confidence_score * 100:.2f}%)"

    class Meta(BaseAbstractModel.Meta):
        verbose_name_plural = "DocumentsClassifications"
        app_label = "document_processing"
