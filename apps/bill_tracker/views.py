from django.shortcuts import render, redirect
from django.contrib import messages

from . import models as m


def index(request):
	if 'user_id' in request.session:
		context = {
			'bill_items': m.BillItem.objects.filter(user_id=request.session['user_id']).order_by('updated_at')
		}
		return render(request, 'bill_tracker/index.html', context)
	return redirect('login_registration:login')


def create_bill_item(request):
	if request.method == 'POST':
		try:
			bill_item = m.BillItem()
			bill_item.description = request.POST['description']
			bill_item.amount = request.POST['amount']
			bill_item.user_id = request.session['user_id']
			bill_item.save()
		except:
			messages.error(request, 'Invalid input')
	return redirect('bill_tracker:index')


def delete_bill_item(request, bill_item_id):
   bill_item = m.BillItem.objects.get(id=bill_item_id)
   bill_item.delete()
   return redirect('bill_tracker:index')


def edit_bill_item(request, bill_item_id):
   bill = m.BillItem.objects.get(id=bill_item_id)
   if request.method == 'POST':
      try:
         bill.description = request.POST['description']
         bill.amount = request.POST['amount']
         bill.save()
         return redirect('bill_tracker:index')
      except:
         messages.error(request, 'Invalid input')

   context = {
       'bill': bill
   }
   return render(request, 'bill_tracker/edit_bill_item.html', context)
