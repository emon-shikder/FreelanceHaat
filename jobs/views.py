from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Proposal
from .forms import JobForm, ProposalForm
from django.db.models import Q
from .models import Job

@login_required
def job_list(request):
    query = request.GET.get('q', '')  # Get the search query
    jobs = Job.objects.filter(status='open').order_by('-created_at')

    # Filter jobs if a search query is provided
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(skills_required__icontains=query)
        )

    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    user_proposal = None
    if request.user.user_type == 'freelancer':
        user_proposal = Proposal.objects.filter(job=job, freelancer=request.user).first()
    
    context = {
        'job': job,
        'user_proposal': user_proposal,
    }
    return render(request, 'jobs/job_detail.html', context)

@login_required
def job_create(request):
    if request.user.user_type != 'client':
        messages.error(request, 'Only clients can post jobs.')
        return redirect('job_list')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.client = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('jobs:job_detail', pk=job.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JobForm()
    
    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if job.client != request.user:
        messages.error(request, 'You do not have permission to edit this job.')
        return redirect('jobs:job_list')
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('jobs:job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if job.client != request.user:
        messages.error(request, 'You do not have permission to delete this job.')
        return redirect('jobs:job_list')
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('jobs:job_list')
    
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})


@login_required
def submit_proposal(request, job_id):
    if request.user.user_type != 'freelancer':
        messages.error(request, 'Only freelancers can submit proposals.')
        return redirect('jobs:job_detail', pk=job_id)
    
    job = get_object_or_404(Job, pk=job_id)
    
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.job = job
            proposal.freelancer = request.user
            proposal.save()
            messages.success(request, 'Proposal submitted successfully!')
            return redirect('jobs:job_detail', pk=job_id)
    else:
        form = ProposalForm()
    
    return render(request, 'jobs/proposal_form.html', {
        'form': form,
        'job': job
    })

@login_required
def accept_proposal(request, job_id, proposal_id):
    if request.user.user_type != 'client':
        messages.error(request, 'Only clients can accept proposals.')
        return redirect('jobs:job_detail', pk=job_id)
    
    job = get_object_or_404(Job, pk=job_id)
    if job.client != request.user:
        messages.error(request, 'You do not have permission to accept this proposal.')
        return redirect('jobs:job_detail', pk=job_id)
    
    proposal = get_object_or_404(Proposal, pk=proposal_id, job=job)
    proposal.accepted = True
    proposal.save()
    job.status = 'in_progress'  # Optionally update the job status
    job.save()
    
    messages.success(request, 'Proposal accepted successfully!')
    return redirect('jobs:job_detail', pk=job_id)

