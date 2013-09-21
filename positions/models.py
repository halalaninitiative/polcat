from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=255)
    description = models.TextField()
