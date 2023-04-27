from django.contrib import admin
from django.urls import path

from . import views

# Etiqueta del conjunto de urls, name_app
app_name = "departamento_app"

urlpatterns = [
    path('list-departamento/', views.DepartamentoListView.as_view(), name='lista_departamento'),
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
]
