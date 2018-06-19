from django.db import models

class User(models.Model):
	name = models.CharField(max_length=64)
	email = models.CharField(max_length=32, unique=True)
	password = models.CharField(max_length=254)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)