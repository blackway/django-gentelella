from rest_framework import serializers

from sakila.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        # fields = ('title', 'description', 'release_year', 'language', 'original_language', 'replacement_cost', 'special_features', )