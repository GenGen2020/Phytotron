# -*- coding: utf-8 -*-

"""
@author: Aaron.An
@contact: QQ:294964314
@Created on: 2024/2/25 22:19
@Remark: 
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.ROLE)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'role', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
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