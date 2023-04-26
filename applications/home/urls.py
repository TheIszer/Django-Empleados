from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.IndexView.as_view()),
    path("list/", views.TestListView.as_view()),
    path("Test-list/", views.ModelTestListView.as_view()),
    path("add-test/", views.TestCreateView.as_view(), name='prueba_add'),
]