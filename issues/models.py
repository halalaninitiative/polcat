from django.db import models

from profiles.models import Profile


class Issue(models.Model):
    issue = models.CharField(max_length=255)
    description = models.TextField()


class Stand(models.Model):
    STAND_CHOICES = (
        ('for', 'For'),
        ('againt', 'Against'),
        ('undecided', 'Undecided'),
    )

    profile = models.ForeignKey(Profile)
    issue = models.ForeignKey(Issue)
    stand = models.CharField(max_length=15, choices=STAND_CHOICES)
    datetime = models.DateTimeField(auto_now_add=True)
