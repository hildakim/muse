from django.contrib import admin
from django.urls import path
from .views import *

app_name = "ticket"

urlpatterns = [
    path('', ticket, name="ticket"),
    path('<str:id>', detail, name="ticket_detail"),
    path('new/', new, name="ticket_new"),
    path('edit/<str:id>', edit, name="ticket_edit"),
    path('delete/<str:id>', delete, name="ticket_delete"),
]