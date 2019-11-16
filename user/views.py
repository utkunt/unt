from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from user.forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
def loginuser(request):

	form = LoginForm(request.POST or None)

	context = {
	"form":form
	}

	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		user = authenticate(username = username, password = password)

		if user is None:
			messages.success(request,"kullanıcı adı veya şifre yanlış")
			return render(request,"login.html",context)

		login(request,user)
		return render(request,"index.html")

	return render(request, "login.html",context)

def logoutuser(request):
	pass

@login_required(login_url  = "user:addarticle")
def addarticle(request):

	form = ArticleForm(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		article = form.save(commit = False)
		article.author = request.user
		article.save()
		return redirect("index")
	return render(request, "addarticle.html",context)
'''