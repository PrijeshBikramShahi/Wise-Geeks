from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userForm
from django.contrib import messages
from baseform.forms import InvForm
from baseform.models import *

def homepage(request):
    if request.user.is_authenticated:
        if investor.objects.filter(investor = request.user).exists():
            return render(request, 'baseform/investor_homepage.html')
        else:
            return render(request, 'baseform/startup_homepage.html')
    return render(request, 'users/homepage.html')


def choosebase(request):
    return render(request, "users/startuppage.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")  # Use "password" instead of "password1"
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage')) #Discover Saksham File # Redirect to a dashboard or home page
        else:
            return render(request, 'users/login.html', {
                "message": "Invalid Credentials."
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register(request, base='default_value'):
    """
    Handles user registration based on the 'base' parameter.
    Redirects to different forms or re-renders the registration page as needed.
    """
    # Initialize the form
    form = userForm()
    print(base)

    if request.method == 'POST':
        print(base)
        print("0")
        form = userForm(request.POST)
        if form.is_valid():
            print("00")
            # Save the form data
            form.save()
            print("000")
            print(base)
            # Handle redirection based on the 'base' parameter
            if base == "investor":
                return render(request, "users/investform.html",{'form': InvForm()})
            elif base == "startup":
                return render(request, "users/startupform.html")
            else:
                print(base)
                # If 'base' is invalid, delete the saved instance and re-render the form
                instance = form.instance  # Get the saved instance
                instance.delete()  # Delete the instance from the database
                return render(request, "users/register.html", {
                    "form": userForm(),  # Reinitialize the form
                    "base": base,
                    "error_message": "Invalid base parameter. Please try again."
                })

        # If the form is invalid, print errors for debugging
        print(form.errors)

    # For GET requests or invalid POST submissions, render the registration form
    return render(request, "users/register.html", {
        "form": form,
        "base": base
    })

# def investor_view(request):
#     return render(request,'users/investform.html')

# def startup_view(request):
#     return render(request,'users/startupform.html')

def discover(request):
    list = investor.objects.all()
    if list is not None:
        return render(request, 'users/discover.html', {'list':list})
    else:
        return render(request, 'users/discover.html', {'list': []})


def about(request):
    return render(request, "users/about.html")

def contact(request):
    return render(request, "users/contact.html")

def blogs(request):
    return render(request, "users/blogs.html")
