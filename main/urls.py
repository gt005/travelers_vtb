from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view(), name='main_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create/', views.CreateDataUnitView.as_view(), name='create'),


]
