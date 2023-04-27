from django.urls import path
from . import views

# Etiqueta del conjunto de urls, name_app
app_name = "persona_app"

urlpatterns = [
    path("",
         views.InicioView.as_view(), 
         name="home"
    ),
    path(
        "listar-todos-empleados/",
        views.ListAllEmpleados.as_view(),
        name="list_all_empleados"
    ),
    path(
        "listar-empleados-admin/",
        views.ListEmpleadosAdmin.as_view(),
        name="empleados_admin"
    ),
    path(
        "listar-por-area/<shortname>/",
        views.ListByAreaEmpleados.as_view(),
        name="list_by_area"
    ),
    path(
        "listar-por-trabajo/<shortname>/",
         views.ListByJobEmpleados.as_view(),
         name="list_by_job"
    ),
    path(
        "buscar-por-palabra-clave/",
        views.ListByKword.as_view(),
        name="list_by_kword"
    ),
    path(
        "lista-de-habilidades/",
         views.ListHabilidadesEmpleado.as_view(),
         name="list_by_skills"
    ),
    path(
        "ver-empleado/<pk>/",
        views.EmpleadoDetailView.as_view(),
        name="empleado_detail"
    ),
    path(
        "add-empleado/",
        views.EmpleadoCreateView.as_view(),
        name="add_empleado"    
    ),
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
        name='delete_empleado'
    ),
]