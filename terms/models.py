from django.db import models

from parties.models import Party
from positions.models import Position
from profiles.models import Profile


class Term(models.Model):
    profile = models.ForeignKey(Profile)
    position = models.ForeignKey(Position)
    party = models.ForeignKey(Party)
    start = models.DateField()
    end = models.DateField()
