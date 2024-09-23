from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home after successful login
    else:
        form = CustomUserLoginForm()

    return render(request, 'auth/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')
