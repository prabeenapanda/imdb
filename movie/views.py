from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from movie.models import Movie
from movie.models import Cast
from movie.serializers import CastSerializer,MovieSerializer


@csrf_exempt
def create_movies(request):
    #print(type(request.body))  # byte
    data = json.loads(request.body)  # str
    movie = Movie.objects.create(name=data["Name"], release_date=data["Release_date"])
    # movie = Movie(name=data["name"],release_date=data["release_date"])
    # movie.save()
    #print(type(json.dumps(data)))  # dict
    #print(data['Name'])#null=True
    return JsonResponse({"message": "Success"})
    # return JsonResponse(data)


@csrf_exempt
def get_movies(request):
    movies = Movie.objects.all()  # select * from movie
    serializer = MovieSerializer(movies, many=True)
    # movies = Movie.objects.get(id=1)#where id is 1
    # #movies.delete()
    # if request.GET.get("name"):  # here "name" is what name we are passing in get request
    #     movies = movies.filter(
    #         name__contains=request.GET.get("name"))  # in name__contains name is the name obj of model
    # if request.GET.get("start_date") and request.GET.get("end_date"):
    #     movies = movies.filter(release_date__gte=request.GET.get("start_date"),
    #                            release_date__lte=request.GET.get("end_date"))
    # movies.exists()  # true or false
    # payload = {"mymovies": []}
    # for movie in movies:
    #     temp = {}
    #     temp["name"] = movie.name
    #     temp["release_date"] = movie.release_date
    #     payload["movies"].append(temp)
    # return JsonResponse(payload)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def update_movies(request):
    data = json.loads(request.body)  # str
    movie = Movie.objects.get(id=data["id"])
    #movie.name=data["Name"]
    serializer = MovieSerializer(movie, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(serializer.errors, safe= False)
    #serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def delete_movies(request):
    data = json.loads(request.body)  # str
    movie = Movie.objects.get(id=data["id"])
    movie.delete()
    return JsonResponse({"message": "Deleted"})




@csrf_exempt
def create_casts(request):
    data = json.loads(request.body)  # str
    cast = Cast.objects.create(cast_name=data["Cast_name"], age=data["Age"], gender=data["Gender"])
    movie = Movie.objects.get(id=data["Movie_id"])
    cast.movies.add(movie)
    return JsonResponse({"message": "Success"})
    # return JsonResponse(data)


@csrf_exempt
def get_casts(request):
    casts = Cast.objects.all()
    serializer = CastSerializer(casts, many=True)
   # vardata = serializer.data
    #print(serializer.data)
    # Mymovies = Movie.objects.get(id=1)
    # mycast = Cast.objects.filter(movies=Mymovies)#something
    # #print(mycast.values())#whole queryset
    # #print(mycast.first().cast_name)#Ranveer
    # print(mycast.values("cast_name","age"))#t [{'cast_name': 'Ranveer', 'age': 34}, {'cast_name': 'Ranveer', 'age': 34}, {'cast_name':
    # # 'Rajes', 'age': 30}, {'cast_name': 'Rajes', 'age': 30}]>
    # print(mycast.values_list("movies__name", flat = True))#<QuerySet ['Something', 'Something', 'Something', 'Something']>

    # payload = {"mycast": []}
    # for cast in casts:
    #     temp = {}
    #     # temp["Movie"] = cast.movies # TypeError: Object of type ManyRelatedManager is not JSON serializable
    #     temp["Cast_name"] = cast.cast_name
    #     temp["Age"] = cast.age
    #     temp["Gender"] = cast.gender
    #     payload["mycast"].append(temp)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def update_casts(request):
    data = json.loads(request.body)  # str
    cast = Cast.objects.get(id=data["id"])
    #movie.name=data["Name"]
    serializer = CastSerializer(cast, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(serializer.errors, safe= False)
    #serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def delete_casts(request):
    data = json.loads(request.body)  # str
    movie = Cast.objects.get(id=data["id"])
    movie.delete()
    return JsonResponse({"message": "Deleted"})