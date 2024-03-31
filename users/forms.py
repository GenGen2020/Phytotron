# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE, required=True)
    queen = forms.BooleanField(required=False, initial=False)  # 假设这是一个可选的布尔字段
    review_file = forms.FileField(required=True)  # 添加审查文件字段，标记为必填

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "role", "queen", "email", "password1", "password2", "review_file"]

def clean_email(self):
        email = self.cleaned_data.get('email')  # 使用get以避免KeyError
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class ApprovedListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ApprovedListForm, self).__init__(*args, **kwargs)
        self.fields['approved'] = forms.ModelMultipleChoiceField(
            queryset=CustomUser.objects.filter(approved=False),
            widget=forms.CheckboxSelectMultiple,
        )

    class Meta:
        model = CustomUser
        fields = []


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['approved']

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)