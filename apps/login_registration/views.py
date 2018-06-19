from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
import bcrypt

from . import models as m
from apps.lilquote import models as qm
from apps.tvshow import models as tm


# supporting function
def setup_web_session(request, user):
	request.session['user_id'] = user.id
	request.session['user_name'] = user.email
	request.session['name'] = user.name

def profile(request):
	if 'user_id' in request.session:
		quotes = qm.Quote.objects.filter(user_id=request.session['user_id'])
		tvshows = tm.TVShow.objects.filter(likes_by__user_id=request.session['user_id'])
		context = {
			'quotes': quotes,
			'tvshows': tvshows,
		}
	else:
		context = {}
	return render(request, 'login_registration/profile.html', context)


def register(request):
	if request.method == 'POST':
		is_valid = True
		# 4 is not blank
		if len(request.POST['name']) == 0:
			messages.error(request, 'Name cannot be empty')
			is_valid = False
		if len(request.POST['email']) == 0:
			messages.error(request, 'Email cannot be empty')
			is_valid = False
		if len(request.POST['password']) == 0:
			messages.error(request, 'Password cannot be empty')
			is_valid = False
		if len(request.POST['confirm']) == 0:
			messages.error(request, 'Confirm Password cannot be empty')
			is_valid = False
		# password length more than 6
		if len(request.POST['password']) < 6:
			messages.error(request, 'Password must be at least 6 character')
			is_valid = False
		# password and confirm is match
		if request.POST['password'] != request.POST['confirm']:
			messages.error(request, 'Password not match')
			is_valid = False

		if is_valid == True:
			try:
				user = m.User()
				user.name = request.POST['name']
				user.email = request.POST['email']
				user.password = request.POST['password']
				user.save()
				setup_web_session(request, user)
				return redirect('login_registration:profile')
			except:
				raise
				messages.error(request, 'Email already exist')
	return render(request, 'login_registration/register.html')

def login(request):	
	if request.method == 'POST':
		is_valid = True
		if len(request.POST['email']) == 0:
			messages.error(request, 'Email cannot blank')
			is_valid = False
		if len(request.POST['password']) == 0:
			messages.error(request, 'Password cannot blank')
			is_valid = False
		if is_valid:
			try:
				user = m.User.objects.get(email=request.POST['email'])
				if user.password == request.POST['password']:
					setup_web_session(request, user)
					return redirect('login_registration:profile')
				else:
					messages.error(request, 'Incorect Password')
			except:
				raise
				messages.error(request, 'User not found')
			return render(request, 'login_registration/login.html')
	return render(request, 'login_registration/login.html')

def logout(request):
	request.session.clear()
	return redirect('login_registration:profile')


def users(request, keyword):
	try:
		users = m.User.objects.filter(Q(email__contains=keyword) | Q(name__contains=keyword))
		context = {
			'keyword': keyword,
			'users': users,
		}
	except:
		messages.error(request, 'Not found')
		context = {}
	return render(request, 'login_registration/users.html', context)

def search(request):
	if request.method == 'POST':
		if len(request.POST['keyword']) > 0:
			keyword =request.POST['keyword']
			return redirect('login_registration:users', keyword=keyword)
		return redirect('login_registration:profile')
