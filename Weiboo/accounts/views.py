from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect

from .forms import RegisterForm, ProfileForm, LoginForm
from .models import UserProfile

@csrf_protect
@require_http_methods(["GET", "POST"])
def login_register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    login_form = LoginForm(request, data=request.POST or None, prefix="login")
    register_form = RegisterForm(request.POST or None, prefix="register")

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login' and login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.GET.get('next', 'accounts:profile')
            return redirect(next_url)

        elif form_type == 'register' and register_form.is_valid():
            user = register_form.save()
            UserProfile.objects.get_or_create(user=user)
            
            # Auto-login after registration
            authenticated_user = authenticate(
                username=register_form.cleaned_data['username'],
                password=register_form.cleaned_data['password1']
            )
            login(request, authenticated_user)
            
            messages.success(request, "Registration successful! Welcome to our community.")
            return redirect('accounts:profile')

        else:
            messages.error(request, "Please correct the errors below.")

    context = {
        'login_form': login_form,
        'register_form': register_form,
    }
    return render(request, 'accounts/login_register.html', context)

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('accounts:login_register')

@login_required
def profile(request):
    profile = request.user.profile  # Using the related_name
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form})