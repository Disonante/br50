from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tiradas/', views.tiradas, name='tiradas'),
    path('tiradas/nueva/', views.nueva_tirada, name='nueva_tirada'),
    path('tiradas/editar/<int:pk>/', views.editar_tirada, name='editar_tirada'),
    path('tiradas/eliminar/<int:pk>/', views.eliminar_tirada, name='eliminar_tirada'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('register/', views.register, name='register'),  # Nueva URL para el registro
    path('register/', views.inicio, name='register'),  # Pendiente implementación de registro
    
]
