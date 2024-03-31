# -*- coding: utf-8 -*-

"""
@author: Aaron.An
@contact: QQ:294964314
@Created on: 2024/3/8 16:33
@Remark: 
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email,
                                          approved=1)
            print(user.check_password(password))
            if user.check_password(password):
                # user.backend = 'django.contrib.auth.backends.ModelBackend'
                return user
        except user_model.DoesNotExist:
            return None
