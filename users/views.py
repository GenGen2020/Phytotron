import random
import string

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from users.forms import RegistrationForm, EmailAuthenticationForm
from users.models import CustomUser


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('users:login_view')  # Redirect to the home page or another desired page
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password, backend='users.backends.EmailBackend')
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('users:approve_list')
            else:
                return redirect('users:index')  # Redirect to the desired URL after successful login
        else:
            form = AuthenticationForm()
            return render(request, 'login/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})


def logout(request):
    return redirect('users:login')


def get_pending_approval_list(request):
    pending_approval_obj = CustomUser.objects.filter(approved=0)
    return render(request, 'approve_users.html', {'users': pending_approval_obj})


def approved_view(request, user_id):
    user_obj = get_object_or_404(CustomUser, pk=user_id)
    user_obj.approved = 1
    username = gen_username(user_obj.role)
    user_obj.username = username
    user_obj.save()
    pending_approval_obj = CustomUser.objects.filter(approved=0)
    return JsonResponse({'msg': "success"})


def declined_view(request, user_id):
    user_obj = get_object_or_404(CustomUser, pk=user_id)
    user_obj.approved = 2
    username = gen_username(user_obj.role)
    user_obj.username = username
    user_obj.save()
    pending_approval_obj = CustomUser.objects.filter(approved=0)
    return JsonResponse({'msg': "success"})


def gen_username(role):
    if role == 0:
        prefix = "student_"
    elif role == 1:
        prefix = "professor_"
    else:
        prefix = "company_"
    return prefix + gen_random_username()


def gen_random_username(length=5):
    # 生成包含大小写字母和数字的字符集
    characters = string.ascii_letters + string.digits
    # 从字符集中随机选择length个字符，并拼接成字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
