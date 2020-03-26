from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


def registration(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Welcome, your are loggedin")
            return redirect('login')
    else:
        form = RegistrationForm() 
    return render(request ,'user/register.html',{"form":form})

@login_required
def profilepage(request):
    return render(request,'user/profile.html',{})