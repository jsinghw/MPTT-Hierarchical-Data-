from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class FileSystem(MPTTModel):
    name = models.CharField(max_length=40, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
