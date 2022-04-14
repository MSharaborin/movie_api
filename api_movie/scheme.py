from ninja import Schema, ModelSchema
from ninja.errors import HttpError

from pydantic import validator

from .models import Movie


class MovieScheme(ModelSchema):
    class Config:
        model = Movie
        model_fields = '__all__'
