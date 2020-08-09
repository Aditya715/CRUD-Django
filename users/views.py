"""
    User registration views
"""

from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib import messages

# Create your views here.
def register_user(request):
    """
        Register
    """
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
       
        if user_form.is_valid() and profile_form.is_valid():
            # saving user form
            user = user_form.save()
            # saving profile form
            profile_form = profile_form.save(commit=False)
            # handling relations here
            profile_form.user = user
            # relations saved.
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            # sending message to the front end.
            messages.success(request, f"Registration complted for {username}. Login with your credentials.")
            return redirect("login")
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()
    
    # contextual to pass to the front end.
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'registration/register.html',context)