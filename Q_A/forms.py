from django import forms
from django.forms import widgets
from .models import Q_A,Q_A_Answer
from django_summernote.widgets import SummernoteWidget

class Q_AForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Q_AForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'id': 'form_title',
            'autofocus': True,
            'style': "width: 91%;"
        })

    class Meta:
        model = Q_A
        fields = ['title', 'content', 'upload_files']
        widgets = {
            'content' : SummernoteWidget(),
        }
    
class Q_A_AnswerForm(forms.ModelForm):
    class Meta:
        model = Q_A_Answer
        fields = ['content']
        widgets = {
            'content' : SummernoteWidget(),
        }
        labels = {
            'content': '답변내용',
        }