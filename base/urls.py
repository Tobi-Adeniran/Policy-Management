from django.urls import path
from .views import Dept, Policy, Home,  CustomLoginView, RegisterForm
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('register/', RegisterForm.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('', Home.as_view(), name = 'index'),
    path('departments/', Dept.as_view(), name = 'dept'),
    path('policies/<int:pk>/', Policy.as_view(), name='policy'),
    path('searchbar/',  views.searchbar, name='searchbar'),
]