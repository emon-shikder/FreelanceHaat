from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('freelancers/', views.freelancer_list, name='freelancer_list'),
    path('freelancers/<int:pk>/', views.freelancer_detail, name='freelancer_detail'),
]