from django.db.models import Count, Q
from .models import Job, Proposal

def get_available_jobs(user=None, skills=None):
    """Get filtered list of available jobs"""
    jobs = Job.objects.filter(status='open')
    
    if skills:
        jobs = jobs.filter(skills_required__icontains=skills)
    
    if user and user.user_type == 'freelancer':
        jobs = jobs.annotate(
            has_proposal=Count(
                'proposals',
                filter=Q(proposals__freelancer=user)
            )
        )
    
    return jobs.order_by('-created_at')

def create_proposal(job, freelancer, data):
    """Create a new proposal"""
    proposal = Proposal(
        job=job,
        freelancer=freelancer,
        cover_letter=data['cover_letter'],
        bid_amount=data['bid_amount']
    )
    proposal.save()
    return proposal