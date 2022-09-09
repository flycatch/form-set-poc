from django.urls import path
from . import views


urlpatterns = [
    path('forms', views.FormWizardView.as_view(), name='forms'),
    path('projects', views.ListProject.as_view(), name='projects'),
    path('projects/<int:pk>', views.ListProjectDetailView.as_view(), name='project-details'),
]
