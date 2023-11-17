import uuid
from django.db import models


class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class UserHistoryMixin(models.Model):
    created_by = models.UUIDField(editable=False, null=True)
    updated_by = models.UUIDField(editable=False, null=True)

    class Meta:
        abstract = True


class DateHistoryMixin(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    updated_datetime = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
