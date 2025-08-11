from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone

from generals.constants import BoolChoices


class PrimaryKeyAbstractModel(models.Model):
    """
    Adds the primary key to any model
    """

    id = models.BigAutoField(  # noqa
        primary_key=True,
        help_text="Table's primary key.",
        verbose_name="Primary Key",
    )

    class Meta:
        abstract = True


class AccountAbstractModel(models.Model):
    """
    Adds the account owner id (Main Key) to any model
    """

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.PROTECT,
        related_name="owner_account",
        help_text="Account ID to which this record belongs.",
        verbose_name="Accounts",
        null=True,
    )

    class Meta:
        abstract = True

class KeyAbstractModel(models.Model):
    """
    Adds a key field so that the user can identify his/her record to any model
    """

    key = models.CharField(
        max_length=20,
        default="",
        help_text="Record's key that should be displayed.",
        verbose_name="Key",
        unique=True,
    )

    class Meta:
        abstract = True


class NameAbstractModel(models.Model):
    """
    Adds the name field to any model
    """

    name = models.CharField(
        max_length=150,
        default="",
        help_text="Record's name that should be displayed.",
        verbose_name="Short name",
    )

    class Meta:
        abstract = True


class RecordHistoryAbstractModel(models.Model):
    """
    Adds the creation and modification fields to any model
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Record creation timestamp.",
        verbose_name="Created at",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Record update timestamp.",
        verbose_name="Updated at",
    )

    class Meta:
        abstract = True


class RecordControlAbstractModel(models.Model):
    """
    Adds control fields and soft delete to manage the data in any model
    """

    is_active = models.BooleanField(
        default=BoolChoices.YES.value,
        help_text="Whether the record is active or not.",
        verbose_name="Is it active?",
    )
    is_deleted = models.BooleanField(
        default=BoolChoices.NO.value,
        help_text="Whether the record is deleted or not.",
        verbose_name="Is it deleted?",
    )
    modified_by = models.CharField(
        max_length=255,
        default="no_email@api.com",
        help_text="Last user that modified this record.",
        verbose_name="Who modified it?",
        validators=[EmailValidator(message="Enter a valid email address.")],
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        help_text="Record deletion timestamp.",
        verbose_name="Deleted at",
    )

    def delete(self, hard_delete=False, *args, **kwargs):
        if hard_delete:
            return super().delete(*args, **kwargs)

        self.is_deleted = True
        self.eliminated_at = timezone.now()
        self.save()
        return self.is_deleted

    class Meta:
        abstract = True


class BaseAbstractModel(
    PrimaryKeyAbstractModel,
    RecordHistoryAbstractModel,
):
    """
    Base model for any table in the database that needs a Primary Key
    """

    fields = [
        "id",
        "created_at",
        "updated_at",
    ]

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class AccountBaseTableModel(BaseAbstractModel, AccountAbstractModel):

    fields = BaseAbstractModel.fields + ["account"]

    class Meta(BaseAbstractModel.Meta):
        abstract = True

