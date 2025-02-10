from django.urls import path
from Guest import views

app_name = "Guest"

urlpatterns = [
    path('',views.login,name="login"),
    path('user/',views.user,name="user"),
]