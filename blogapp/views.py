from django.shortcuts import render,redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_views(request):



	return render(request,'home.html',{})

def blog_views(request):
	blog=Blog.objects.all()
	context={
	 'allblog':blog
	}


	return render(request,'blog.html',context)