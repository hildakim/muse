from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update_view, name='profile_update'),
    path('delete', profile_delete, name='profile_delete'),
]

