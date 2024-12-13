from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('jobs/<int:job_id>/review/', views.create_review, name='create_review'),
]