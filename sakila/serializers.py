from rest_framework import serializers

from sakila.models import Film
from sakila.models_views import CustomerList


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        # fields = ('title', 'description', 'release_year', 'language', 'original_language', 'replacement_cost', 'special_features', )


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerList
        fields = '__all__'