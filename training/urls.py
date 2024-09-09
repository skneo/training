from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_trainings),
    path('trainees', views.trainees),
    path('add_training', views.add_training),
    path('edit_trainees', views.edit_training),
    path('add_trainees', views.add_trainees),
]