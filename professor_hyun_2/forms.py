from django import forms
from .models import professor_hyun_2

from django_summernote.widgets import SummernoteWidget

class professor_hyun_2_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(professor_hyun_2_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content_created'].label = '출판년월'
        self.fields['content_created'].widget.attrs.update({
            'placeholder': '출판년월을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = professor_hyun_2
        fields = ['pid', 'content', 'content_created', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
            'content_created' : '출판년월',
        }