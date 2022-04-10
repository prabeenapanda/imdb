from rest_framework import serializers
from movie.models import Cast, Movie


# class CastSerializer(serializers.Serializer):
#     #movies = serializers.CharField()
#     cast_name = serializers.CharField(max_length=32)
#     age = serializers.IntegerField()
#     gender = serializers.CharField(max_length=12)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'release_date','rating']


class CastSerializer(serializers.ModelSerializer):
    #movies = MovieSerializer(read_only=True)

    class Meta:
        model = Cast
        fields = ['id', 'movies', 'cast_name', 'age', 'gender']
