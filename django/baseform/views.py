from django.shortcuts import render, redirect
from .models import investor, startup
from .forms import InvForm, StartForm
from django.urls import reverse
from django.contrib.auth.models import User

def investor_view(request):
    if request.method == 'POST':
        invform = InvForm(request.POST, request.FILES)
        if invform.is_valid():
            invform.save()
            return render(request, "baseform/investor_homepage.html")  # Redirect to a success page
    else:
        invform = InvForm()
    return render(request, 'users/investform.html', {'form': invform})

def investorviewpage(request):
    return render(request, "baseform/investor_homepage.html")

def startupviewpage(request):
    return render(request, "baseform/startup_homepage.html")

def startup_view(request):
    if request.method == 'POST':
        startform = StartForm(request.POST, request.FILES)
        if startform.is_valid():
            startform.save()
            return redirect('discover')  # Redirect to a success page
    else:
        startform = StartForm()
    return render(request, 'users/startupform.html', {'form': startform})

def startup_gallery(request):
    return render(request, "baseform/startupviewgallery.html")

def dashboard(request):
    return render(request, "baseform/dashboard.html")

