from django import forms
from .models import professor_hyun_7

from django_summernote.widgets import SummernoteWidget

class professor_hyun_7_form(forms.ModelForm):
    class Meta:
        model = professor_hyun_7
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }