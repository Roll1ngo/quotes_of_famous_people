from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("registration/", views.registration, name="registration")
]
