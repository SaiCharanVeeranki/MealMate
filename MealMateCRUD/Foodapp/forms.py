from django import forms
from Foodapp.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','price','item_image']