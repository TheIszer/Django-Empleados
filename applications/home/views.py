from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from .models import Test
from .forms import TestForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'home/home.html'

class TestListView(ListView):
    template_name = 'home/list.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'testList'


class ModelTestListView(ListView):
    model = Test
    template_name = "home/testList.html"
    context_object_name = 'test_list'


class TestCreateView(CreateView):
    model = Test
    template_name = "home/add.html"
    # fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = TestForm
    success_url = '/'
