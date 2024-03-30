from django.urls import path
from .views import  LoginView, LogoutView


urlpatterns = [
    # path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='Login'),
    path('login/', LoginView.as_view()),
]