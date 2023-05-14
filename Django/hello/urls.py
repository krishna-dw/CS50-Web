from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("krishna", views.krishna, name="krishna"),
    path("dewabrata", views.dewabrata, name="dewabrata"),
]