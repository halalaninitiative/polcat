from django.db import models


class Party(models.Model):
    party = models.CharField(max_length=255)
    description = models.TextField()
