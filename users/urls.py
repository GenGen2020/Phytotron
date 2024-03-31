# -*- coding: utf-8 -*-

"""
@author: Aaron.An
@contact: QQ:294964314
@Created on: 2024/2/25 23:05
@Remark: 
"""
from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login_view'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('approve_users/', views.get_pending_approval_list, name='approve_list'),
    path('user_approved/<int:user_id>/', views.approved_view, name='user_approved'),
    path('user_declined/<int:user_id>/', views.declined_view, name='user_declined'),
    path('main', views.main_page, name='main'),
    path('mypage', views.my_page, name='mypage'),
    path('room', views.submit_room, name='room'),
    path('changeuser/', views.changeuser, name='changeuser'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('submitInfo/', views.submit_form, name='submitInfo'),
    path('api/fetch/', views.fetch, name='fetch'),
    path('admin/logout/', views.custom_logout_view, name='admin_logout'),
    path('download/', views.download, name='download'),
    path('logout/', views.logout, name='download'),
]
