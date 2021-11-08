from django import forms
from .models import professor_lee_6

from django_summernote.widgets import SummernoteWidget

class professor_lee_6_form(forms.ModelForm):
    class Meta:
        model = professor_lee_6
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }