from .forms import UserCreateForm,UserLoginForm
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_view(request, *args, **kwargs):
    form  = UserLoginForm(request, data = request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect('/')
    context = {"form":form, "btn_label":"Login","title":"Login"}
    return render(request, 'accounts/login.html',context)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect('/account/login/')
    context = {"form":None ,"description":"Are you sure you want to logout?", "btn_label":"Click to confirm","title":"Logout"}
    return render(request, 'accounts/login.html',context)

def register_view(request, *args, **kwargs):
    form  = UserCreateForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request, user)
        return redirect('/account/login/')
    context = {"form":form, "btn_label":"Register","title":"Register"}
    return render(request, 'accounts/login.html',context)
