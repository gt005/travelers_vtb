from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main_page'),
    path('offers/', views.OffersListView.as_view(), name='offers'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<user_id>', views.ProfileView.as_view(), name='profile'),
    path('create/', views.CreateDataUnitView.as_view(), name='create'),
    path('view_offer/<offer_id>', views.OfferView.as_view(), name='offer_view'),
]
