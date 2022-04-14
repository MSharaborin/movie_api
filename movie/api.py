from ninja import NinjaAPI
from api_movie.api import api_movie as auth_router


api = NinjaAPI(title='Movie Api', version='1.0.0',)

api.add_router('', auth_router)