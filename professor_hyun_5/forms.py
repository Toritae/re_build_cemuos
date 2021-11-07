from django import forms
from .models import professor_hyun_5_1,professor_hyun_5_2

from django_summernote.widgets import SummernoteWidget

class professor_hyun_5_1_form(forms.ModelForm):
    class Meta:
        model = professor_hyun_5_1
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }

class professor_hyun_5_2_form(forms.ModelForm):
    class Meta:
        model = professor_hyun_5_2
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'content' : '내용',
        }