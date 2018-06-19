from django.db import models
from apps.login_registration.models import User

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=128)

	user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
	description = models.CharField(max_length=255)

	project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
