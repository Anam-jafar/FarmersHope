from django import forms
from .models import Question, Response


class QuestionDetailForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'img', 'video']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
