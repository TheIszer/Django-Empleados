from django.urls import path
from . import views

# Etiqueta del conjunto de urls, name_app
app_name = "persona_app"

urlpatterns = [
    path("",
         views.InicioView.as_view(), 
         name="home"
         ),
    path("listar-todos-empleados/", views.ListAllEmpleados.as_view()),
    path("listar-por-area/<shortname>/", views.ListByAreaEmpleados.as_view()),
    path("listar-por-trabajo/<shortname>/", views.ListByJobEmpleados.as_view()),
    path("buscar-por-palabra-clave/", views.ListByKword.as_view()),
    path("lista-de-habilidades/", views.ListHabilidadesEmpleado.as_view()),
    path("ver-empleado/<pk>/", views.EmpleadoDetailView.as_view()),
    path("add-empleado/", views.EmpleadoCreateView.as_view()),
    path(
        "success/", 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        "update-empleado/<pk>/", 
        views.EmpleadoUpdateView.as_view(), 
        name='update_empleado'
    ),
    path(
        "delete-empleado/<pk>/", 
        views.EmpleadoDeleteView.as_view(), 
        name='update_empleado'
    ),
]