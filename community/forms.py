from django.forms import ModelForm
from community.models import *
from django import forms

class Form(ModelForm):
    class Meta:
        model = Article
        fields=['category','title','contents']
        widgets = {
            'category' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'input-category',
                }
            ),
            'title' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'input-title'
                }
            ),
            'contents' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'input-contents'
                }
            )
        }