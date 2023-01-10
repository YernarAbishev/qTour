from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def homePage(request):
    articles = Article.objects.all().order_by('-postDate')[:4]
    tours = Tour.objects.all().order_by('-postDate')[:3]
    return render(request, "app/home.html", {
        'articles': articles,
        'tours': tours,
    })

def aboutPage(request):
    page = AboutPage.objects.all()
    return render(request, "app/about.html", {
        'page': page
    })

def allArticles(request):
    articles = Article.objects.all().order_by('-postDate')
    return render(request, "app/articles.html", {
        'articles': articles
    })

def articleDetail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "app/article-detail.html", {
        'article': article
    })

def allTours(request):
    tours = Tour.objects.all().order_by('-postDate')
    return render(request, "app/tours.html", {
        'tours': tours
    })

def tourDetails(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, "app/tour-detail.html", {
        'tour': tour
    })

def allCampings(request):
    campings = Camping.objects.all().order_by('-postDate')
    return render(request, "app/camping.html", {
        'campings': campings
    })

def campingDetail(request, pk):
    camping = get_object_or_404(Camping, pk=pk)
    return render(request, "app/camping-detail.html", {
        'camping': camping
    })

def loanPage(request):
    loans = LoanItems.objects.all()
    return render(request, "app/loan.html", {
        'loans': loans
    })

def loanDetails(request, pk):
    loan = get_object_or_404(LoanItems, pk=pk)
    return render(request, "app/loan-detail.html", {
        'loan': loan
    })

def mapPage(request):
    return render(request, "app/map.html")

def taxiPage(request):
    return render(request, "app/taxi.html")

def foodPage(request):
    return render(request, "app/food.html")

def signUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Аккаунт создан! Войдите в систему')
            return redirect('logIn')
    else:
        form = UserRegistrationForm()

    return render(request, "user/sign-up.html", {
        'form': form
    })

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Здравствуйте, {username}.")
                return redirect("homePage")
            else:
                messages.error(request, "Некорректный логин или пароль")
        else:
            messages.error(request, "Некорректный логин или пароль")
    form = AuthenticationForm()
    return render(request, "user/login.html", {
        "form": form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "Вы вышли из системы")
    return redirect("homePage")

def profile(request):
    return render(request, "user/profile.html")

def museum(request):
    museums = Museum.objects.all()
    return render(request, "app/museum.html", {
        'museums': museums
    })