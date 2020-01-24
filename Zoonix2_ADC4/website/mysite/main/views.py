from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Parlour
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import OurForm
from .models import Book
import json
from django.views.decorator.csrf import csrf_exempt




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

def upload_book(request):

	form = OurForm()
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('main:book_list')
	return render(request, "main/upload.html", {"form": form})

#pagination
def book_objects_pagination(request,PAGENO, SIZE):
		skip = SIZE * (PAGENO -1)
		books = Book.objects.all() [skip:(PAGENO * SIZE)]
		dict ={
			"books":list(Book.values("title","name"))
			}
		return JsonResponse(dict)

def update_book(request, id=None):
	instance = get_objects_or_404(Book, id=id)
	form = OurForm()
	if request.method == "POST":
		form =OurForm(request.POST, request.FILES, instance = instance)
		if form.isvalid 


def book_list(request):
	book = Book.objects.all()
	return render (request, "main/book_list.html", {"books": book})



def delete_book(request, pk):
	book = Book.objects.get(pk=pk)
	book.delete()
	return redirect("main:book_list")

def api_data(request):
	book = Book.objects.all()
	dict_value = {
		"books": list( book.values("title", "name"))

	}
	return JsonResponse(dict_value)


@csrf_exempt
def api_update_data(request, pk=None):
	book = Book.objects.get(pk=pk)
	if request.method == "GET":
		return JsonResponse ({"title": book.title, "name": book.name})

	else:
		decoded_data = request.body.decode('utf-8')
		book_data = json.loads(decoded_data)
		book.title = book_data ['title'] 
		book.name = book_data ['name']
		book.save()
		return JsonResponse({"message": "completed"})