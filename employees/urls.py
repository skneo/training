from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.all_employees),
    path('add_employee', views.add_employee),
    path('view_employee', views.view_employee),
    path('edit_employee', views.edit_employee),
]