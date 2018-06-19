import requests, json
from django.shortcuts import render, redirect

from . import models

# SUPPORTING FUNCTION
# URL
TVMAZE_SEARCH_URL = 'http://api.tvmaze.com/search/{}?q={}'
TVMAZE_GET_URL = 'http://api.tvmaze.com/{}/{}'

def get_request(url):
   response = requests.get(url)
   return json.loads(response.text)
# URL
def get_tvshow_by_api_id(api_id):
   try:
      tvshow = models.TVShow.objects.get(api_id=api_id)
      return tvshow
   except:
      tvshow = models.TVShow()
      url = TVMAZE_GET_URL.format('shows', api_id)
      response = get_request(url)
      tvshow.tvmaze_parse_json(response)
      tvshow.save()
      return tvshow

def search_tvshows(keyword):
   tvshows = []
   url = TVMAZE_SEARCH_URL.format('shows', keyword)
   for result in get_request(url):
      try:
         tvshow = models.TVShow.objects.get(api_id=result['show']['id'])
      except:
         tvshow = models.TVShow()
         tvshow.tvmaze_parse_json(result['show'])
         tvshow.save()
      tvshows.append(tvshow)
   return tvshows

def like_a_tvshow(user_id, api_id):
   tvshow = models.TVShow.objects.get(api_id = api_id)
   try:
      models.TVShowLike.objects.get(tvshow_id=tvshow.id, user_id=user_id)
      return False
   except:
      like = models.TVShowLike()
      like.user_id = user_id
      like.tvshow_id = tvshow.id
      like.save()
      return True

def unlike_a_tvshow(user_id, api_id):
   tvshow = models.TVShow.objects.get(api_id = api_id)
   try:
      like = models.TVShowLike.objects.get(tvshow_id=tvshow.id, user_id=user_id)
      like.delete()
      return True
   except:
      return False

def get_user_tvshowlikes_apiid(user_id):
   user_likes = []
   for like in models.TVShowLike.objects.filter(user_id=user_id):
      user_likes.append(like.tvshow.api_id)
   return user_likes

# VIEW FUNCTION
def tvshows(request):
   tvshows = models.TVShow.objects.all()
   context = {
      'tvshows': tvshows,
   }
   print('========================================')
   print(get_user_tvshowlikes_apiid(request.session['user_id']))
   return render(request, 'tvshow/tvshows.html', context)

def search(request, keyword):
   tvshows = search_tvshows(keyword)
   context = {
      'user_likes': get_user_tvshowlikes_apiid(request.session['user_id']),
      'tvshows': tvshows
   }
   return render(request, 'tvshow/tvshows.html', context)

def post_search(request):
   if request.method == 'POST':
      return redirect('tvshow:search', keyword=request.POST['keyword'])

def like(request, user_id, api_id):
   like_a_tvshow(user_id, api_id)
   return redirect(request.META['HTTP_REFERER'])

def unlike(request, user_id, api_id):
   unlike_a_tvshow(user_id, api_id)
   return redirect(request.META['HTTP_REFERER'])
