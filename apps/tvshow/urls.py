from django.urls import path
from . import views

app_name = 'tvshow'

urlpatterns = [
   path('', views.tvshows, name='tvshows'),
   path('post_search/', views.post_search, name='post_search'),
   path('search/<str:keyword>', views.search, name='search'),
   path('like/<int:user_id>/<int:api_id>', views.like, name='like'),
   path('unlike/<int:user_id>/<int:api_id>', views.unlike, name='unlike'),
]