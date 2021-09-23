from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
