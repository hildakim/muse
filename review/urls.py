from django.contrib import admin
from django.urls import path
from .views import *

app_name = "review"

urlpatterns = [
    path('detail/<str:id>', detail, name='detail'),
    path('new/<str:mt20id>', new, name='new'),
    path('allreviews', allReviews, name="allreviews"),
    path('', index, name='index'),
    path('search/', showSearch, name="search"),
    path('delete/<str:id>/<str:mt20id>', delete, name="delete"),
]