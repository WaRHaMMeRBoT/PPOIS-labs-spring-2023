from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.CharField(max_length=30, null=True, blank=True)
    date_of_visit = models.CharField(max_length=30, null=True, blank=True)
    name_of_doctor = models.CharField(max_length=30, null=True, blank=True)
    conclusion = models.CharField(max_length=30, null=True, blank=True)
