from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("<seccion>/", views.inicio, name="inicio_seccion"),
]