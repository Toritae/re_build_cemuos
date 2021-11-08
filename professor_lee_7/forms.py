from django import forms
from .models import professor_lee_7

from django_summernote.widgets import SummernoteWidget

class professor_lee_7_form(forms.ModelForm):
    class Meta:
        model = professor_lee_7
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }