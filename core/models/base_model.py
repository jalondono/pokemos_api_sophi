from datetime import datetime

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    Basic model that most others inherit. Used to track creation and modification
    """
    created_at: datetime = models.DateTimeField(default=timezone.now)
    """When was this object created?"""
    updated_at: datetime = models.DateTimeField(auto_now=True)
    """When was this object last updated?"""

    class Meta:
        abstract = True
