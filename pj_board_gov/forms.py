from django import forms
from .models import pj_post_gov

from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['front_content'].widget.attrs.update({
            'placeholder': '전면부 내용을 입력해주세요.',
            'class': 'form-control',
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = pj_post_gov
        fields = ['title', 'photo', 'front_content', 'content', 'create_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'front_content': SummernoteWidget(),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput
        }
        labels = {
            'title': '제목',
            'photo' : '썸네일',
            'front_content' : '전면부 내용' ,
            'content' : '내용',
        }