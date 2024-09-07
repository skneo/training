from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login', views.login_user),
    # path('logout', views.logout_user),
    # path('change_password', views.change_password),
    path('employees/', include('employees.urls')),
    path('training/', include('training.urls')),
]
