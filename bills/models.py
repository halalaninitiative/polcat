from django.db import models

from profiles.models import Profile


class Bill(models.Model):
    STATUS_CHOICES = (
        ('1st', '1st Reading'),
        ('2nd', '2nd Reading'),
        ('3rd', '3rd Reading'),
        ('passed', 'Passed'),
        ('failed', 'Failed'),
        ('unknown', 'Unknown'),
    )

    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Profile)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
