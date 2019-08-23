# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    actor_id = models.TextField(unique=True)  # This field type is a guess.
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'actor'


class Address(models.Model):
    address_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city_id = models.IntegerField()
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    category_id = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=25)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    city_id = models.IntegerField(unique=True)
    city = models.CharField(max_length=50)
    country_id = models.SmallIntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.SmallIntegerField(unique=True)
    country = models.CharField(max_length=50)
    last_update = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    store_id = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address_id = models.IntegerField()
    active = models.CharField(max_length=1)
    create_date = models.TextField()  # This field type is a guess.
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    # film_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.CharField(max_length=4, blank=True, null=True)
    language_id = models.SmallIntegerField()
    original_language_id = models.SmallIntegerField(blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.TextField()  # This field type is a guess.
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.TextField()  # This field type is a guess.
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film'


class FilmActor(models.Model):
    actor_id = models.IntegerField()
    film_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor_id', 'film_id'),)


class FilmCategory(models.Model):
    film_id = models.IntegerField()
    category_id = models.SmallIntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film_id', 'category_id'),)


class FilmText(models.Model):
    film_id = models.SmallIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_text'


class Inventory(models.Model):
    inventory_id = models.IntegerField(unique=True)
    film_id = models.IntegerField()
    store_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=20)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.IntegerField(unique=True)
    customer_id = models.IntegerField()
    staff_id = models.SmallIntegerField()
    rental_id = models.IntegerField(blank=True, null=True)
    amount = models.TextField()  # This field type is a guess.
    payment_date = models.TextField()  # This field type is a guess.
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.IntegerField(unique=True)
    rental_date = models.TextField()  # This field type is a guess.
    inventory_id = models.IntegerField()
    customer_id = models.IntegerField()
    return_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    staff_id = models.SmallIntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory_id', 'customer_id'),)


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


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    manager_staff_id = models.SmallIntegerField()
    address_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'store'
