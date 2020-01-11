from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Parlour
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Parlour
from .forms import OurForm

# Create your views here.
def homepage(request):
	return render(request=request, template_name="main/home.html",
		context={"parlours":Parlour.objects.all} )

def register(request):
	if request.method == "POST":
		form = OurForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('main:homepage')
			
	form = OurForm()
	return render(request=request, template_name="main/register.html",
		context={"form":form})
		
def user_logout(request):
	logout(request)
	return redirect('main:homepage')

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.clean_data.get("username")
			password = form.clean_data.get("password")
			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				messages.success(request, f'you have logged as {{username}}')
				return redirect('main:homepage')

	form= AuthenticationForm()
	return render(request, "main/login.html",
		context={"form": form})

