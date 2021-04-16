from django import forms
from .models import Project, Apply


class ProjectPost(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'sub_title', 'body', 'category']


class ApplyPost(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['role', 'body']
