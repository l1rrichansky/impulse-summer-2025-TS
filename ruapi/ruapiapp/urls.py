from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/<int:person_id>/", views.user_detail, name="user_detail"),
    path("random", views.random, name="random")
]