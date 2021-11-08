from django import forms
from .models import professor_lee_5_1,professor_lee_5_2

from django_summernote.widgets import SummernoteWidget

class professor_lee_5_1_form(forms.ModelForm):
    class Meta:
        model = professor_lee_5_1
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }

class professor_lee_5_2_form(forms.ModelForm):
    class Meta:
        model = professor_lee_5_2
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }