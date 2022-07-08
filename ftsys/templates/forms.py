from django.forms import ModelForm
from .models import *
from django import forms

class CreateItem(ModelForm):
    class Meta:
        model = Item
        fields = ['fname', 'mname', 'age', 'add', 'contact', 'disease', 'specifydisease', 'plan', 'total']