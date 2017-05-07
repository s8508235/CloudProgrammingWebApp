from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from forms import SignUpForm,PostForm
# Create your views here.

def home(request):
	return render(request, 'blog/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('fat')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def post_list(request):
    posts=None
    # posts = Post.objects.all()
    if request.user.is_authenticated():
    	posts = Post.objects.filter(author=User.objects.get(username=request.user.get_username()))
    if posts is not None:
    	return render(request,'blog/post_list.html',{'posts':posts})
    else:
    	return HttpResponse("<H1>Login!</H1>") 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = form.cleaned_data.get('published_date')
            post.save()
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})