from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.job_create, name='job_create'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('<int:pk>/edit/', views.job_edit, name='job_edit'),
    path('<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('<int:job_id>/propose/', views.submit_proposal, name='submit_proposal'),
    path('<int:job_id>/proposals/<int:proposal_id>/accept/', views.accept_proposal, name='accept_proposal'),
]