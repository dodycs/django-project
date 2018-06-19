from django.db import models
from apps.login_registration.models import User
from datetime import datetime

class TVShow(models.Model):
	api_url = models.CharField(max_length=128, unique=True)
	api_id = models.IntegerField(unique=True)

	name = models.CharField(max_length=64)
	image = models.CharField(max_length=64)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def tvmaze_parse_json(self, data):
		self.api_url = data['_links']['self']['href']
		self.api_id = data['id']
		self.name = data['name']

		try:
			self.image = data['image']['original']
		except:
			self.image = 'http://via.placeholder.com/210x295'

class TVShowLike(models.Model):
	tvshow = models.ForeignKey(TVShow, related_name='likes_by', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
