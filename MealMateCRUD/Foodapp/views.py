from django.shortcuts import render, redirect
from Foodapp.models import Item
from Foodapp.forms import ItemForm
# Create your views here.
def home(request):
    li = Item.objects.all()
    data = {
        'li' : li
    }
    return render(request,'home.html',data)

def details(request,item_id):
    item = Item.objects.get(pk = item_id)
    data = {
        'item': item
        }
    return render(request,'details.html',data)

def add_items(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Foodapp:home')
    return render(request, 'item_form.html',{'form':form})

def update_items(request, item_id):
    item = Item.objects.get(pk = item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('Foodapp:home')
    return render(request, 'item_form.html',{'form':form})


def delete_item(request, item_id):
    item = Item.objects.get(pk = item_id)
    if request.method == "POST":
        item.delete()
        return redirect('Foodapp:home')
    return render(request, 'delete_msg.html',{'item':item})