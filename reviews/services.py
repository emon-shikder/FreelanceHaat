from .models import Review

def create_review(job, reviewer, reviewed, data):
    """Create a new review"""
    review = Review(
        job=job,
        reviewer=reviewer,
        reviewed=reviewed,
        rating=data['rating'],
        comment=data['comment']
    )
    review.save()
    return review

def get_user_reviews(user):
    """Get all reviews for a user"""
    return Review.objects.filter(reviewed=user).select_related('reviewer', 'job')