from django import forms
from .models import User
from django.contrib.auth import get_user_model

us = get_user_model


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'nickname', 'email', 'phone']

        def clean_username(self):
            username = self.cleaned_data.get('username')
            if us.objects.filter(username=username).exists():
                raise forms.ValidationError('아이디가 이미 사용중입니다')
            return username
