from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from jobs.models import Job

@login_required
def create_review(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    
    if request.user != job.client and request.user != job.proposals.filter(accepted=True).first().freelancer:
        messages.error(request, 'You are not authorized to leave a review for this job.')
        return redirect('jobs:job_detail', pk=job_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.job = job
            review.reviewer = request.user
            review.reviewed = job.client if request.user != job.client else job.proposals.filter(accepted=True).first().freelancer
            review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('jobs:job_detail', pk=job_id)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/review_form.html', {
        'form': form,
        'job': job
    })