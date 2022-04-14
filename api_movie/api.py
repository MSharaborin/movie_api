from typing import List
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Form, Router
from ninja.errors import HttpError

from .scheme import MovieScheme
from .models import Movie


api_movie = Router(tags=['Movie'])


@api_movie.get('/all_movie', response=List[MovieScheme])
def get_all_movie(request):
    return Movie.objects.all()
