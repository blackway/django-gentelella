from django.contrib import admin
from django import forms as django_forms
from django.db.models import Count
from django.forms import BaseModelFormSet
# from django_filters import DateRangeFilter
from rangefilter.filter import DateRangeFilter

from conf import settings
from .models import Film, Language


class LanguageChoiceField(django_forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return 'Language: {}'.format(obj.name)


class MyAdminFormSet(BaseModelFormSet):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update', )
    exclude = ('id', )


class DateTimeRangeFilter(object):
    pass


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    # using = 'erp_oracle'

    # def save_model(self, request, obj, form, change):
    #     # Tell Django to save objects to the 'other' database.
    #     obj.save(using=self.using)
    #
    # def delete_model(self, request, obj):
    #     # Tell Django to delete objects from the 'other' database
    #     obj.delete(using=self.using)
    #
    # def get_queryset(self, request):
    #     # Tell Django to look for objects on the 'other' database.
    #     return super().get_queryset(request).using(self.using)
    #
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     # Tell Django to populate ForeignKey widgets using a query
    #     # on the 'other' database.
    #     return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
    #
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     # Tell Django to populate ManyToMany widgets using a query
    #     # on the 'other' database.
    #     return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

    # fields = ('title', 'description', 'release_year', 'language_name', 'original_language_id', 'replacement_cost', 'special_features', )

    line_numbering = 0
    list_per_page = settings.LIST_PER_PAGE
    # list_per_page = 10  # record 10 per page
    list_display = ('line_number', 'title', 'description', 'release_year', 'language', 'original_language', 'replacement_cost', 'special_features', 'last_update', )
    # exclude = ('id',)
    # list_select_related = ('language',)
    # readonly_fields = ('parent',)

    # inline_type = 'tabular'  # or could be 'stacked'
    # inline_reverse = ['language_name']  # could do [('book', {'fields': ['title', 'authors'})] if you only wanted to show certain fields in the create admin

    list_editable = ('language', 'original_language', )
    readonly_fields = ('line_number',)
    # list_editable = ('special_features', )
    # list_filter = ('last_update', 'release_year', 'language_id',)
    # list_filter = ('last_update', 'release_year', 'language',)
    # list_editable = ('req_status', )
    list_filter = (
        'language',
        ('last_update', DateRangeFilter),
        # ('last_update', DateTimeRangeFilter),
        # ('birth_date', DateRangeFilter),
    )
    ordering = ['-last_update', ]
    search_fields = ['title', ]
    date_hierarchy = 'last_update'

    def line_number(self, obj):
        self.line_numbering += 1
        return self.line_numbering

    line_number.short_description = '#'

    # def get_queryset(self, request):
    #     qs = super(FilmAdmin, self).get_queryset(request)
    #     return qs.annotate(books_count=Count('id'))

    # 드롭 다운에서 ForeignKey 표시 텍스트를 변경하는 방법은 무엇입니까?
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'language':
    #         return LanguageChoiceField(queryset=Language.objects.all())
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    #     # return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'language':
    #         return LanguageChoiceField(queryset=Language.objects.all()) # if you want to alphabetize your query
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_changelist_formset(self, request, **kwargs):
        kwargs['formset'] = MyAdminFormSet
        return super().get_changelist_formset(request, **kwargs)

    def get_language_name(self, obj):
        return obj.language.name
    get_language_name.short_description = '언어 이름'


# admin.site.register(Film, FilmAdmin)
