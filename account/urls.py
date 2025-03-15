from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from account.views import register, get_users

urlpatterns = [
    path("register/", register),
    path('login/', TokenObtainPairView.as_view()),
    path('users/', get_users),
]
