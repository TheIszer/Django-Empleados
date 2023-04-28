from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from applications.departamento.models import Departamento

from .forms import NewDepartamentoForm

# Create your views here.
# Ver el listado de departamentos

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista_departamento.html"
    context_object_name = 'departamentos'


# Crear un Nuevo Departemento/
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        # Primera forma
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shortname'],
        )
        depa.save()

        # Segunda forma
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job='1',
            departamento = depa,
        )
        return super(NewDepartamentoView, self).form_valid(form)
