from django.db.models import fields
from django.forms import ModelForm
from .models import Item 

class CreateItem(ModelForm):
    class Meta:
        model = Item
        fields = ['sname', 'fname', 'mname', 'age', 'add', 'contact', 'disease', 'specifydisease', 'plan', 'total']
        