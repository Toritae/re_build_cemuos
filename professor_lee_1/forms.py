from django import forms
from .models import professor_lee_1_1,professor_lee_1_2, professor_lee_1_3, professor_lee_1_4, professor_lee_1_5

from django_summernote.widgets import SummernoteWidget

class professor_lee_1_1_form(forms.ModelForm):
    class Meta:
        model = professor_lee_1_1
        fields = ['content', 'create_date']
        widgets = {
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
            'content_created' : '게재년도',
        }

class professor_lee_1_2_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(professor_lee_1_2_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content_created'].label = '게재년도'
        self.fields['content_created'].widget.attrs.update({
            'placeholder': '게재년도을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = professor_lee_1_2
        fields = ['pid', 'content', 'content_created', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'content_created' : forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
            'content_created' : '게재년도',
        }

class professor_lee_1_3_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(professor_lee_1_3_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content_created'].label = '게재년도'
        self.fields['content_created'].widget.attrs.update({
            'placeholder': '게재년도을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = professor_lee_1_3
        fields = ['pid', 'content', 'content_created', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'content_created' : forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
            'content_created' : '게재년도',
        }

class professor_lee_1_4_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(professor_lee_1_4_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content_created'].label = '게재년도'
        self.fields['content_created'].widget.attrs.update({
            'placeholder': '게재년도을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = professor_lee_1_4
        fields = ['pid', 'content', 'content_created', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'content_created' : forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
            'content_created' : '게재년도',
        }

class professor_lee_1_5_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(professor_lee_1_5_form, self).__init__(*args, **kwargs)
        self.fields['pid'].label = '번호'
        self.fields['pid'].widget.attrs.update({
            'placeholder': '번호을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content_created'].label = '게재년도'
        self.fields['content_created'].widget.attrs.update({
            'placeholder': '게재년도을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': '내용을 입력해주세요.',
            'class': 'form-control',
        })
    class Meta:
        model = professor_lee_1_5
        fields = ['pid', 'content', 'content_created', 'create_date']
        widgets = {
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'content_created' : forms.TextInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(),
            'create_date': forms.HiddenInput,
        }
        labels = {
            'pid' : '번호',
            'content' : '내용',
            'content_created' : '게재년도',
        }

