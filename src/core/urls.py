from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("saludar/", views.saludar),
    path("saludar-con-etiqueta/", views.saludar_con_etiqueta),
    path("saludar2/<str:nombre>/<str:apellido>/", views.saludar_con_parametros),
    path("tirar-dado/", views.tirar_dado, name="tirar_dado"),
    path("ejercicio-1/", views.ejercicio_1, name="ejercicio_1"),
    path("notas/", views.notas, name="notas"),
    path("ejercicio-2/", views.ejercicio_2, name="ejercicio_2"),
    path("mi_json/", views.mi_json, name="mi_json"),
]

urlpatterns += [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="core/pages/logout.html"),
        name="logout",
    ),
]
