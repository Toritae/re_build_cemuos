from django import forms
from .models import professor_lee_4

from django_summernote.widgets import SummernoteWidget

class professor_lee_4_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(professor_lee_4_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
    class Meta:
        model = professor_lee_4
        fields = ['pid', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
        }