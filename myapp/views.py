from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from myapp.forms import RegisterForm, AddCustomerForm
from myapp.models import Customer


# Create your views here.
def home(request):
    customers = Customer.objects.all()
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
    context = {'customers': customers}
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


def view_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(pk=pk)
        context = {'customer': customer}
        return render(request=request, template_name='myapp/customer.html', context=context)
    messages.warning(request=request, message="You must be logged in first.")
    return redirect('home')


def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save()
                messages.warning(request=request, message="Customer added.")
                return redirect('home')
        context = {'form': form}
        return render(request=request, template_name='myapp/add_customer.html', context=context)
    else:
        messages.warning(request=request, message="You must be logged in first.")
        return redirect('home')


def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(pk=pk)
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Customer updated.")
            return redirect('home')
        context = {'form': form}
        return render(request=request, template_name='myapp/update_customer.html', context=context)
    messages.warning(request=request, message="You must be logged in first.")
    return redirect('home')


def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        messages.success(request, "Customer deleted.")
        return redirect('home')
    else:
        messages.warning(request, "You must be logged in first.")
        return redirect('home')
