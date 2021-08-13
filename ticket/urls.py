from django.contrib import admin
from django.urls import path
from .views import *

app_name = "ticket"

urlpatterns = [
    path('', ticket, name="ticket"),
    path('<int:id>', detail, name="ticket_detail"),
    path('new/', new, name="ticket_new"),
    path('edit/<int:id>', edit, name="ticket_edit"),
    path('delete/<int:id>', delete, name="ticket_delete"),
    path('search', search, name = 'search'),
]