from django.urls import path, include
from . import views
app_name = 'account'

urlpatterns = [
    path('signup', views.sign_up, name= 'signup'),
]