from django.urls import path
from .views import  LoginView, RegisterView, LogoutView


urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]