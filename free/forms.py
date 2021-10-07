from django import forms
from django.forms import widgets
from .models import Free
from django_summernote.widgets import SummernoteWidget

class FreeWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FreeWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
            'style': "width: 91%;"
        })

    class Meta:
        model = Free
        fields = ['title', 'content', 'upload_files']
        widgets = {
            'content' : SummernoteWidget(),
        }