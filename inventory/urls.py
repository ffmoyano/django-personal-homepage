from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_elements, name='project_elements'),
    path('projects/<int:project_id>', views.project_elements, name='project_elements'),
]