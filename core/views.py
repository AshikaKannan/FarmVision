

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages



def dashboard(request):
    return render(request, 'dashboard.html')  # Ensure you have a 'dashboard.html' template.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'core/login.html')

