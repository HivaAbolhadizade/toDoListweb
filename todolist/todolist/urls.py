from django.urls import path, include
from . import views
app_name = 'todolist'

urlpatterns = [
    path('home_page', views.main_page, name= 'home_page'),
    path('main_page', views.main_page, name= 'main_page'),
]