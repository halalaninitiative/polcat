from django.db import models


class Profile(models.Model):
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=7)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=255)
    sex = models.CharField(max_length=7, choices=SEX_CHOICES)
    education = models.TextField() # for now
