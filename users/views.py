from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserUpdateForm
from .models import CustomUser
from reviews.models import Review
from django.db.models import Avg


def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    
    reviews = Review.objects.filter(reviewed=request.user)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    # Get profile picture URL
    profile_picture_url = request.user.profile_picture.url if request.user.profile_picture else None
    
    context = {
        'form': form,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'profile_picture_url': profile_picture_url  # Include profile picture in context
    }
    return render(request, 'users/profile.html', context)


def freelancer_list(request):
    freelancers = CustomUser.objects.filter(user_type='freelancer')
    return render(request, 'users/freelancer_list.html', {'freelancers': freelancers})

def freelancer_detail(request, pk):
    freelancer = get_object_or_404(CustomUser, pk=pk, user_type='freelancer')
    reviews = Review.objects.filter(reviewed=freelancer)
    return render(request, 'users/freelancer_detail.html', {
        'freelancer': freelancer,
        'reviews': reviews
    })