from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("<str:title>/edit/", views.edit, name="edit"),
    path("search/", views.search, name="search"),
    path("random/", views.random, name="random"),
    path("create/", views.create, name="create"),
]
