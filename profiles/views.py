from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)