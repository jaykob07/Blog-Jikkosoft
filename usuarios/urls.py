from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


# acordate que LogoutView requiere un POST en su defecto usa LoginView!

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register' ),
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name='logout'),
]