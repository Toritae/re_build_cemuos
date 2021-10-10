from django import forms
from .models import seminar_post

from django_summernote.widgets import SummernoteWidget

class sem_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(sem_form, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = seminar_post
        fields = ['title', 'content', 'upload_files', 'create_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title': '제목',
            'photo' : '썸네일',
            'content' : '내용',
        }