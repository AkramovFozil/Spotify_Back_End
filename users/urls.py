from django.urls import path
from .views import UserView, UserRegisterView, UserLoginInView

urlpatterns = [
    path('users/', UserView.as_view(), ),
    path('register/', UserRegisterView.as_view(), ),
    path('login/',UserLoginInView.as_view(),name='login'),
]
