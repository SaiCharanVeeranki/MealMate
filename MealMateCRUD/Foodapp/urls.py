from django.urls import path
from . import views

app_name = 'Foodapp'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('details/<int:item_id>/',views.details, name = 'details'),
    path('add/',views.add_items, name = 'add_items'),
    path('update/<int:item_id>/',views.update_items, name = 'update_items'),
    path('delete/<int:item_id>/',views.delete_item,name= 'delete_item'),
]
