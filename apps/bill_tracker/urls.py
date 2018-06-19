from django.urls import path
from . import views

app_name = 'bill_tracker_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_bill_item', views.create_bill_item, name='create_bill_item'),
    path('delete_bill_item/<int:bill_item_id>',
         views.delete_bill_item, name='delete_bill_item'),
    path('edit_bill_item/<int:bill_item_id>',
         views.edit_bill_item, name='edit_bill_item'),
]
