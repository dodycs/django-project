from django.shortcuts import render, redirect
from django.contrib import messages

from apps.lilquote import models as m

def quotes(request):
	quotes = m.Quote.objects.all()
	context = {
		'quotes': quotes
	}
	return render(request, 'lilquote/quotes.html', context)

def create_quote(request):
	if request.method == 'POST':
		try:
			quote = m.Quote()
			quote.content = request.POST['content']
			quote.user_id = request.session['user_id']
			quote.save()
		except:
			messages.error(request, 'Failed post a quote')
		return redirect('lilquote:quotes')

def delete_quote(request, quote_id):
   try:
      quote = m.Quote.objects.get(id=quote_id, user_id = request.session['user_id'])
      quote.delete()
   except:
      messages.error(request, 'Failed delete a quote')
   return redirect('lilquote:quotes')

def edit_quote(request, quote_id):
	quote = m.Quote.objects.get(id=quote_id, user_id = request.session['user_id'])
	if request.method == 'POST':
		try:
			quote.content = request.POST['content']
			quote.save()
			return redirect('lilquote:quotes')
		except:
			messages.error(request, 'Failed edit the quote')
	context = {
		'quote': quote
	}
	return render(request, 'lilquote/edit.html', context)