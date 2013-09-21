from django.db import models

from profiles.models import Profile


class Saln(models.Model):
    profile = models.ForeignKey(Profile)
    net_worth = models.DecimalField(max_digits=15, decimal_places=3)
    date = models.DateField()
