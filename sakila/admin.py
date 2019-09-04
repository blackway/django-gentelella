from django.contrib import admin
from django import forms as django_forms
from django.forms import BaseModelFormSet
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

    list_display = ('title', 'description', 'release_year', 'language', 'original_language', 'replacement_cost', 'special_features', )
    # exclude = ('id',)
    # list_select_related = ('language',)
    # readonly_fields = ('parent',)

    # inline_type = 'tabular'  # or could be 'stacked'
    # inline_reverse = ['language_name']  # could do [('book', {'fields': ['title', 'authors'})] if you only wanted to show certain fields in the create admin

    list_editable = ('language', 'original_language', )
    # list_editable = ('special_features', )
    # list_filter = ('last_update', 'release_year', 'language_id',)
    # list_filter = ('last_update', 'release_year', 'language',)
    # list_editable = ('req_status', )
    ordering = ['-last_update', ]
    search_fields = ['title', ]
    date_hierarchy = 'last_update'

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
