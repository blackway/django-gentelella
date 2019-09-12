# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum, Func, F, Count


class CreateDateComm(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')  # This field type is a guess.

    class Meta:
        abstract = True


class LastUpdateComm(models.Model):
    last_update = models.DateTimeField(auto_now=True, verbose_name='수정일자')  # This field type is a guess.

    class Meta:
        abstract = True


class Actor(LastUpdateComm):
    actor_id = models.TextField(unique=True)  # This field type is a guess.
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'actor'


class Country(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='country_id')
    # country_id = models.SmallIntegerField(unique=True)
    country = models.CharField(max_length=50)
    last_update = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'country'


class City(models.Model):
    id = models.IntegerField(primary_key=True, db_column='city_id')
    # city_id = models.IntegerField(unique=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='country_id')
    # country_id = models.SmallIntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'city'


class Address(models.Model):
    id = models.IntegerField(primary_key=True, db_column='address_id')
    # address_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')
    # city_id = models.IntegerField()
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


class Category(LastUpdateComm):
    category_id = models.SmallIntegerField(primary_key=True)
    # category_id = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=25)
    # last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'category'


class Store(models.Model):
    id = models.IntegerField(primary_key=True, db_column='store_id')
    # store_id = models.IntegerField(unique=True)
    manager_staff_id = models.SmallIntegerField()
    address = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='address_id')
    # address_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'store'


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(total_amount=Func(Sum('payment__amount'), function='ROUND')
                                               , payment_count=Count('payment__payment_id'))
        # return super().get_queryset().annotate(total_amount=Sum('payment__amount'))


class Customer(CreateDateComm, LastUpdateComm):
    customer_id = models.IntegerField(primary_key=True)
    # customer_id = models.IntegerField(unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_id')
    # store_id = models.IntegerField()
    first_name = models.CharField(max_length=45, verbose_name='첫번째 이름')
    last_name = models.CharField(max_length=45, verbose_name='마지막 이름')
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='address_id')
    # address_id = models.IntegerField()
    active = models.CharField(max_length=1)
    # create_date = models.DateTimeField(auto_now_add=True)# This field type is a guess.
    # last_update = models.DateTimeField(auto_now=True)  # This field type is a guess.

    objects = CustomerManager()
    # objects_payment_amount = CustomerManager()

    # def clean(self):
    #     """
    #     모델에서 유효성 체크
    #     :return:
    #     """
    #     if self.last_name is not None:
    #         raise ValidationError({'last_name': _('Draft entries may not have a publication date.')})

    # def clean(self):
    #     # Don't allow draft entries to have a pub_date.
    #     # if self.status == 'draft' and self.pub_date is not None:
    #     if self.last_name is not None:
    #         raise ValidationError({'last_name': _('Draft entries may not have a publication date.')})
    #         # raise ValidationError(_('Draft entries may not have a publication date.'))

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


class Language(LastUpdateComm):
    # language_id = models.SmallIntegerField(primary_key=True)
    id = models.IntegerField(primary_key=True, db_column='language_id')
    # id = models.SmallIntegerField(primary_key=True, db_column='language_id')
    # language_id = models.SmallIntegerField(unique=True)
    name = models.CharField(max_length=20)
    # last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'language'

    def __str__(self):
        return '%s' % (self.name)


class Film(models.Model):
    id = models.IntegerField(primary_key=True, db_column='film_id')
    # film_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.CharField(max_length=4, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    # language = models.ForeignKey(Language, on_delete=models.CASCADE, db_column='language_id')
    # language_id = models.SmallIntegerField()
    # original_language = models.ForeignKey(Language, on_delete=models.CASCADE, db_column='original_language_id', null=True)
    original_language = models.ForeignKey(Language, on_delete=models.CASCADE, db_column='original_language_id',
                                          related_name='language_as_original_language', blank=True, null=True)
    # original_language_id = models.SmallIntegerField(blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.TextField()  # This field type is a guess.
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.TextField()  # This field type is a guess.
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    # last_update = models.TextField()  # This field type is a guess.
    last_update = models.DateTimeField(auto_now=True, verbose_name='수정일자')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film'

    def __str__(self):
        """
        객체 클래스 기본 내용 출력
        :return:
        """
        return '%s - %s' % (self.id, self.title)

    def language_name(self):
        return self.language.name


class FilmActor(LastUpdateComm):
    actor_id = models.ForeignKey(Actor, on_delete=models.DO_NOTHING)
    # actor_id = models.IntegerField()
    film_id = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    # film_id = models.IntegerField()
    # last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor_id', 'film_id'),)


class FilmCategory(LastUpdateComm):
    film_id = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    # film_id = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    # category_id = models.SmallIntegerField()
    # last_update = models.TextField()  # This field type is a guess.

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
    id = models.IntegerField(primary_key=True, db_column='inventory_id')
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING, db_column='film_id')
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, db_column='store_id')
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inventory'


class Payment(LastUpdateComm):
    """
    from sakila.models import *
    from django.db.models import Sum, Count
    customers = Customer.objects.annotate(num_payment=Count('payment'))

    Customer.objects.annotate(total_amount=Sum('payment__amount'))

    Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
    """
    payment = models.IntegerField(db_column='payment_id', primary_key=True)
    # payment_id = models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # customer_id = models.IntegerField()
    staff_id = models.SmallIntegerField()
    rental_id = models.IntegerField(blank=True, null=True)
    amount = models.TextField()  # This field type is a guess.
    payment_date = models.TextField()  # This field type is a guess.
    # last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'payment'


class Staff(models.Model):
    id = models.SmallIntegerField(primary_key=True, db_column='staff_id')
    # staff_id = models.SmallIntegerField(unique=True)
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


class Rental(LastUpdateComm):
    id = models.IntegerField(primary_key=True, db_column='rental_id')
    # rental_id = models.IntegerField(unique=True)
    rental_date = models.TextField()  # This field type is a guess.
    inventory = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING, db_column='inventory_id')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, db_column='customer_id')
    return_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, db_column='staff_id')
    # last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)
        # unique_together = (('rental_date', 'inventory_id', 'customer_id'),)




