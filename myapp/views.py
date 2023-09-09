from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from myapp.forms import RegisterForm


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request=request, message="You have been logged in.")
            return redirect('home')
        else:
            messages.error(request=request, message="Invalid username or password. Try again.")
            return redirect('home')
    context = {}
    return render(request=request, template_name='myapp/home.html', context=context)


def sign_out(request):
    logout(request)
    messages.success(request=request, message="You have been logged out.")
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request=request, user=user)
            messages.success(request=request, message="You have successfully signed up.")
            return redirect('home')
    else:
        form = RegisterForm()
        context = {"form": form}
        return render(request=request, template_name="myapp/register.html", context=context)
    context = {'form': form}
    return render(request=request, template_name='myapp/register.html', context=context)
