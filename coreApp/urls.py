from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('tours/', views.allTours, name='allTours'),
    path('tour/<int:pk>/', views.tourDetails, name='tourDetails'),
    path('campings/', views.allCampings, name='allCampings'),
    path('camping/<int:pk>/', views.campingDetail, name='campingDetail'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('museum/', views.museum, name='museum'),
    path('loan/', views.loanPage, name='loanPage'),
    path('loan/<int:pk>/', views.loanDetails, name='loanDetails'),
    path('map/', views.mapPage, name='mapPage'),
    path('taxi/', views.taxiPage, name='taxiPage'),
    path('food/', views.foodPage, name='foodPage'),
    path('articles/', views.allArticles, name='allArticles'),
    path('article/<int:pk>/', views.articleDetail, name='articleDetail'),
    path('sign-up/', views.signUp, name='signUp'),
    path('login/', views.logIn, name='logIn'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='user/change-password.html', success_url = '/'), name='change_password'),
]