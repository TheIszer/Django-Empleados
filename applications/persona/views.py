from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    TemplateView,
    UpdateView,
    DeleteView,
    )

# Models
from .models import Empleado
'''
REQUIREMENTS:
1.- listar todos los empleados de la empresa
2.- listar todos los empleados que pertenencen a un area
3.- listar empleados por trabajo
4.- listar empleados por palabra clave
5.- listar habilidades de un empleado
'''

# Create your views here.

# Pagina de Inicio (No es lo mas correcto, pero sirve)
class InicioView(TemplateView):
    template_name = "inicio.html"


# Lista de todos los empleados
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    # model = Empleado
    # Buscar
    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        queryset = Empleado.objects.filter(
            first_name__icontains=key_word
        )
        return queryset
    

# Lista los empleados en forma de admin
class ListEmpleadosAdmin(ListView):
    template_name = 'persona/list_empleados_admin.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


# Lista de empleados por area
class ListByAreaEmpleados(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        area = self.kwargs['shortname']     # Recoover arguments from url
        queryset = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return queryset
    
# Listar empleados por trabajo
class ListByJobEmpleados(ListView):
    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        job = self.kwargs['shortname']     # Recoover arguments from url
        queryset = Empleado.objects.filter(
            departamento__shor_name = job
        )
        return queryset


# Listar empleados por palabra clave
class ListByKword(ListView):
    template_name = "persona/list_by_kword.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        key_word = self.request.GET.get("kword", '')
        queryset = Empleado.objects.filter(
            first_name = key_word
        )
        return queryset

# listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = "persona/list_by_skills.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        key_word_id = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(id=int(key_word_id))
        return empleado.habilidades.all()
        return []
    
# Ver detalles
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


class SuccessView(TemplateView):
    template_name = "persona/success.html"


# Registrar Empleado
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # fields = ['first_name', 'last_name', 'job']     # Specific fields
    # fields = ('__all__')
    # success_url = '.'                                  # Same URL
    # success_url = '/success'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        # Logica
        empleado = form.save(commit=False)      # Almacenar lo del formulario desde la BD
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()             # Actualizar en la BD
        return super(EmpleadoCreateView, self).form_valid(form)

# Editar un Empleado
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

# Eliminar un Empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

