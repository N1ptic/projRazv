from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def get_article_details(request, id):
    article = get_object_or_404(Article, id=id)
    data = {
        'title': article.title,
        'image_url': article.image.url,
        'content': article.content
    }
    return JsonResponse(data)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})

@login_required
def page1(request):
    articles = Article.objects.all()
    return render(request, 'page1.html', {'articles': articles})

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
        
        except Exception as e:
            messages.error(request, str(e))
            return redirect("register")
        
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("page1")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("login")
        

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

def homepage(request):
    return render(request, 'home.html')