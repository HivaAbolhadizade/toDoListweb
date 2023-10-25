from django.urls import path, include
from . import views
app_name = 'todolist'

urlpatterns = [
    path('main_page', views.main_page, name= 'main_page'),
]