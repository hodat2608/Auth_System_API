from django.urls import path
from . import views 
from djoser import views as djoser_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('get_name_user/', views.Get_Username.as_view()),
]