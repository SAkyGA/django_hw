from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserCreateAPIView.as_view()),
    path('auth/', views.AuthAPIView.as_view()),
]