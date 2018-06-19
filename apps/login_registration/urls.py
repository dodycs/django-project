from django.urls import path
from . import views

app_name = 'login_registration'

urlpatterns = [
	path('', views.profile, name='profile'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('search/', views.search, name='search'),
	path('users/<str:keyword>', views.users, name='users'),
]