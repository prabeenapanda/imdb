from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=32)
    release_date = models.DateField()
    rating = models.FloatField(default=1)


gender_choice = (("Male", "MALE"), ("Female", "FEMALE"), ("Transgender", "TRANSGENDER"))


class Cast(models.Model):
    movies = models.ManyToManyField(Movie, related_name="casts",null=True)
    #movie = Movie.objects.get(pk=1)
    #movies.casts.all()#casts = movie.casts.all() casts will contain a queryset of Cast model.
    cast_name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=12,choices=gender_choice)
