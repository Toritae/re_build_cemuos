from django import forms
from .models import member_post_alum_MA_city

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
        self.fields['email'].widget.attrs.update({
            'placeholder': 'E-Mail을 입력해주세요.',
            'class': 'form-control',
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = member_post_alum_MA_city
        fields = ['title', 'photo', 'email', 'content', 'create_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput
        }
        labels = {
            'title': '제목',
            'photo' : '썸네일',
            'email' : 'E-Mail' ,
            'content' : '내용',
        }