from django.urls import path
from e_commerce.API.api1 import *
from e_commerce.API.api2 import *
from e_commerce.API.api3 import *
from e_commerce.API.marvel_api_views import *


urlpatterns = [
    path('api1/',api1),
    path('api2/',api2),
    path('api3/',api3),
    path('marvel_api_views/',get_comics),
    path('marvel_api_views/',purchased_item)
]