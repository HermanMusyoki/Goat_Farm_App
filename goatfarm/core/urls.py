from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_goat, name='add_goat'),
    path('example/', views.example_view, name='example'),
]