from django.urls import path

from .views import index

app_name = "cliente"


urlpatterns = [
    path("", index, name="index"),
]
