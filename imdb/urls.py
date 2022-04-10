"""imdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/create/',views.create_movies),
    path('movie/get/',views.get_movies),
    path('movie/delete/',views.delete_movies),
    path('movie/update/',views.update_movies),
    path('cast/create/',views.create_casts),
    path('cast/get/',views.get_casts),
    path('cast/update/',views.update_casts),
    path('cast/delete/',views.delete_casts),
]
