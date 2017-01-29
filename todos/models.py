from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
