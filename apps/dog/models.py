from __future__ import unicode_literals

from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length = 45)
    breed = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
