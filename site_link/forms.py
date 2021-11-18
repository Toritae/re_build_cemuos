from django import forms
from .models import Sitelink, Sitelink_2, Sitelink_3, Sitelink_4, Sitelink_5, Sitelink_6

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
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }
        
class Sitelink_form_2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Sitelink_form_2, self).__init__(*args, **kwargs)
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
        model = Sitelink_2
        fields = ['title', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }
        
class Sitelink_form_3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Sitelink_form_3, self).__init__(*args, **kwargs)
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
        model = Sitelink_3
        fields = ['title', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }
        
class Sitelink_form_4(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Sitelink_form_4, self).__init__(*args, **kwargs)
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
        model = Sitelink_4
        fields = ['title', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }
        
class Sitelink_form_5(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Sitelink_form_5, self).__init__(*args, **kwargs)
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
        model = Sitelink_5
        fields = ['title', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }
        
class Sitelink_form_6(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Sitelink_form_6, self).__init__(*args, **kwargs)
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
        model = Sitelink_6
        fields = ['title', 'content', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'title' : '사이트명',
            'content' : '사이트 URL',
        }