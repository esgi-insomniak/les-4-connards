from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

from books.models import Books, Loan
from lecture.models import Lecture

def register_request(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render(request, "main/register.html", {"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def index(request):
	books = Books.objects.all().order_by('?')[:4]
	return render(request, 'main/index.html', {'books': books})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")

def profile(request):
	#récupérer les lecture auxquelle l'utilisateur participe
	lecture = Lecture.objects.filter(participants__in=[request.user])
	livre_emprunte = Loan.objects.filter(borrowed_by=request.user)
	now = datetime.now()
	return render(request, 'user/profile.html', {'lectures': lecture, 'livre_emprunte': livre_emprunte, 'now': now})