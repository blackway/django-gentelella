# from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Staff(models.Model):
    staff_id = models.SmallIntegerField(unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address_id = models.IntegerField()
    picture = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.IntegerField()
    active = models.SmallIntegerField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'staff'

