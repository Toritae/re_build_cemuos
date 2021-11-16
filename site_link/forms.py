from django import forms
from .models import Sitelink

from django_summernote.widgets import SummernoteWidget

class Sitelink_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Sitelink_form, self).__init__(*args, **kwargs)
        self.fields['title'].label = '사이트명'
        self.fields['title'].widget.attrs.update({
            'placeholder': '사이트명을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '사이트 URL을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = Sitelink
        fields = ['title', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }