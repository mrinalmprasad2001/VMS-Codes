from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def main_home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("CB:",request)
            return redirect("user_home")
        else:
            messages.error(request, "Invalid username or password")
            print("Error")

    return render(request, "login.html")

def user_register_page(request):
    return render(request,'user_register.html')

def servicer_register_page(request):
    return render(request,'servicer_register.html')

def user_sidebar(request):
    return render(request,'user_sidebar.html')

def user_home(request):
    return render(request, 'user_home.html')

def user_search_service(request):
    return render(request,'user_search.html')

def user_work_status(request):
    return render(request,'user_work_status.html')

def user_payment(request):
    return render(request,'user_payment.html')

def user_profile_edit(request):
    return render(request,'user_profile_edit.html')

def servicer_sidebar(request):
    return render(request,'servicer_sidebar.html')

def servicer_home(request):
    return render(request,'servicer_home.html')

def servicer_worklist(request):
    return render(request,'servicer_worklist.html')

def servicer_payment(request):
    return render(request,'servicer_payment.html')

def servicer_profile_edit(request):
    return render(request,'servicer_profile_edit.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return render(request, "success.html", {"msg": "Registration Successful!"})
    else:
        form = RegistrationForm()
    return render(request, "user_register.html", {"form": form})
