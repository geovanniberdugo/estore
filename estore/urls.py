from django.contrib import admin
from django.urls import path

#App imports
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', views.login, name='login'),
    path('admin/', admin.site.urls),
]