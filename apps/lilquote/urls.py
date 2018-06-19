from django.urls import path
from . import views

app_name = 'lilquote'

urlpatterns = [
   path('', views.quotes, name='quotes'),
   path('create_quote/', views.create_quote, name='create_quote'),
   path('<int:quote_id>/edit/', views.edit_quote, name='edit_quote'),
   path('<int:quote_id>/delete/', views.delete_quote, name='delete_quote'),
]
