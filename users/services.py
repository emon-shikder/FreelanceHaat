from django.db.models import Avg
from .models import CustomUser
from reviews.models import Review

def get_user_profile_data(user):
    """Get aggregated profile data for a user"""
    reviews = Review.objects.filter(reviewed=user)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    return {
        'user': user,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1) if avg_rating else 0,
        'review_count': reviews.count()
    }

def get_freelancer_list(skills=None):
    """Get filtered list of freelancers"""
    freelancers = CustomUser.objects.filter(user_type='freelancer')
    if skills:
        freelancers = freelancers.filter(skills__icontains=skills)
    return freelancers