from django import forms
from .models import kor_conference, kor_jounal

from django_summernote.widgets import SummernoteWidget

class thesis_ma_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(thesis_ma_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '논문번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '논문번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content_created'].label = '게재년도'
        self.fields['content_created'].widget.attrs.update({
            'placeholder': '게재년도를 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = kor_conference
        fields = ['pid', 'content', 'content_created', 'upload_files', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '논문번호',
            'content' : '내용',
            'content_created' : '게재년도',
        }