# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CustomerList(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    # id = models.IntegerField(primary_key=True, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    sid = models.IntegerField(db_column='SID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'customer_list'

    # @property
    # def checkbox(self):
    #     # 체크박스
    #     return 0



class FilmList(models.Model):
    fid = models.IntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.CharField(max_length=25, blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    length = models.SmallIntegerField(blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    actors = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'film_list'


class SalesByFilmCategory(models.Model):
    category = models.CharField(max_length=25, blank=True, null=True)
    total_sales = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_by_film_category'


class SalesByStore(models.Model):
    store_id = models.IntegerField(blank=True, null=True)
    store = models.TextField(blank=True, null=True)  # This field type is a guess.
    manager = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_sales = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_by_store'


class StaffList(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    # id = models.SmallIntegerField(primary_key=True, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    sid = models.IntegerField(db_column='SID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'staff_list'
