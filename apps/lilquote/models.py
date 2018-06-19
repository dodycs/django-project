from django.db import models
from apps.login_registration.models import User

class Quote(models.Model):
   content = models.CharField(max_length=254)

   user = models.ForeignKey(User, related_name='quotes', on_delete=models.CASCADE)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)