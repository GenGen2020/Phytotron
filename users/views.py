import os
import random
import string
import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import logout as out
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from users.forms import RegistrationForm, EmailAuthenticationForm
from users.models import CustomUser, ResearchRequest, Order


@csrf_exempt
def changeuser(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('users:login')
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')

    # Assuming 'request.user' is the user you want to update
    user = request.user

    try:
        # Update user's information (customize this part as needed)
        user.username = name
        user.email = email
        user.telephone = phone
        user.save()

        return JsonResponse({'success': 'User information updated successfully'})
    except Exception as e:
        return JsonResponse({'error': 'An error occurred while updating your information.'})


@csrf_exempt
def changepassword(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('users:login')
    currentPassword = request.POST.get('currentPassword')
    newPassword = request.POST.get('newPassword')
    confirmNewPassword = request.POST.get('confirmNewPassword')
    if not current_user.check_password(currentPassword):
        return JsonResponse({'error': 'User information updated fail Original password error'})
    else:
        if newPassword == confirmNewPassword:
            current_user.set_password(confirmNewPassword)
        else:
            return JsonResponse({'error': 'User information updated fail Password inconsistency'})
    return JsonResponse({'success': 'User information updated successfully'})


# Create your views here.
def register(request):
    if request.method == 'POST':
        result = request.POST.dict()
        print(result)
        uid = str(uuid.uuid4())
        result["username"] = result["first_name"] + uid[0:4]
        form = RegistrationForm(result)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            return redirect('users:main')  # Redirect to the home page or another desired page
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
                return redirect('users:main')  # Redirect to the desired URL after successful login
        else:
            form = AuthenticationForm()
            return render(request, 'login/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})


def main_page(request):
    current_user = request.user
    if request.user.is_authenticated:
        # 当前用户已登录
        print(f"当前登录的用户是: {current_user.username}")
    else:
        return redirect('users:login')
    return render(request, 'main.html')


def my_page(request):
    current_user = request.user
    if request.user.is_authenticated:
        # 当前用户已登录
        print(f"当前登录的用户是: {current_user.username}")
    else:
        return redirect('users:login')
    users_with_supervisor = CustomUser.objects.filter(supervisor=current_user.supervisor)
    all = {'student_list': [student.username for student in users_with_supervisor],
           'supervisor': current_user.supervisor}
    return render(request, 'my_page.html', all)


def download(request):
    if request.user.is_authenticated:
        # 指定想要下载的文件的名称
        order_number = request.GET.get('order_number')
        order = get_object_or_404(Order, order_number=order_number).attachment
        # 检查文件是否存在
        if order and hasattr(order, 'file'):
            # 构建完整的文件路径
            file_path = order.path
            print(file_path)
            with open(file_path, 'rb') as fh:
                # 创建一个HttpResponse对象，内容是文件的内容
                response = HttpResponse(fh.read(), content_type="application/force-download")
                # 设置Content-Disposition头，这样浏览器会将其视为下载而非直接显示
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        else:
            # 如果订单没有attachment，返回适当的响应（例如错误消息或重定向）
            return HttpResponse("No attachment found for this order.", status=404)
    else:
        return redirect('users:login')


def get_dates_between(start_date, end_date):
    # Ensure start_date and end_date are datetime.date objects
    # If you're not sure, you can add checks or conversions here

    # Calculate the difference between end date and start date
    delta = end_date - start_date

    end_date_next = end_date + timedelta(days=1)

    end_date_next = end_date_next.strftime('%Y-%m-%d')

    # Generate a list of dates from start_date to end_date
    date_list = [(start_date + timedelta(days=i)).isoformat() for i in range(delta.days + 1)]

    return date_list, end_date_next


def submit_room(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('users:login')
    id = request.GET.get('id')
    type = request.GET.get('type')
    room_id = type + id
    lab_room_requests = list(
        ResearchRequest.objects.filter(lab_room_number=room_id, approved=1).values('start_date', 'end_date'))
    all_data = []
    pedding_date = []
    clean_date = []
    for lab in lab_room_requests:
        result, end_date_next = get_dates_between(lab["start_date"], lab["end_date"])
        clean_date.append(end_date_next)
        all_data = all_data + result
    all_data = list(set(all_data))
    peddings = list(
        ResearchRequest.objects.filter(lab_room_number=room_id, approved=0).values('start_date', 'end_date'))
    for pedding in peddings:
        result, end_date_next = get_dates_between(pedding["start_date"], pedding["end_date"])
        pedding_date = pedding_date + result
    all_data = list(set(all_data))
    clean_date = [item for item in clean_date if item not in all_data]
    bench = {"2": 5, "3": 5, "4": 10, "5": 5}
    radio_options = []
    if type == "Greenhouse":
        radio_options = [{'value': f'bench {i}', 'label': f'bench {i}'} for i in range(1, int(bench[id]) + 1)]
    print(radio_options)

    result = {"roomid": room_id, "refuse": all_data, "clean_date": clean_date, "pedding_date": pedding_date,
              "radio_options": radio_options, 'type': type}

    return render(request, 'room.html', result)


@csrf_exempt
def submit_form(request):
    # Assuming you have a way to get the current user's ID
    # This could be request.user.id if you're using Django's authentication
    try:
        user_id = request.user.id
        user = request.user

        try:
            # Attempt to retrieve the user based on the ID
            applicant_account = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        # Convert QueryDict to dictionary
        form_data = request.POST.dict()
        print(form_data)

        def convert_date(date_str):
            try:
                # Adjusted for MM/DD/YYYY format
                return datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
            except ValueError:
                return None  # or handle the error as appropriate

        animal = True if form_data.get('animal', '') is not None else False

        current_date = form_data.get('currentDate', '')
        start_date = convert_date(form_data.get('startDate', ''))
        end_date = convert_date(form_data.get('endDate', ''))

        # You might need to process dates and other non-string fields accordingly
        # For simplicity, this example assumes all data is correctly formatted
        overlapping_requests = ResearchRequest.objects.filter(
            lab_room_number=form_data.get('labRoomNumber', ''),
            approved=1,
        ).filter(
            Q(start_date__lte=end_date, end_date__gte=start_date)
        )
        pedding_requests = ResearchRequest.objects.filter(
            lab_room_number=form_data.get('labRoomNumber', ''),
            approved=0,
        ).filter(
            Q(start_date__lte=end_date, end_date__gte=start_date)
        )
        if overlapping_requests or pedding_requests:
            return JsonResponse({'error': 'The room has been occupied within the date'})
        # Create a new ResearchRequest instance
        unit_price = 11
        between_days = datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')
        days = abs(between_days.days)
        if user.queen is 1:
            unit_price = 11
        else:
            unit_price = 13
        print(unit_price)
        price = days * unit_price
        research_request = ResearchRequest(
            applicant_account=applicant_account,
            primary_investigator=form_data.get('primaryInvestigator', ''),
            primary_contact=form_data.get('primaryContact', ''),
            department=form_data.get('department', ''),
            is_active=animal,
            price=price,
            lab_room_number=form_data.get('labRoomNumber', ''),
            contact_phone=form_data.get('contactPhone', ''),
            contact_after_hours=form_data.get('contactAfterHours', ''),
            email=form_data.get('email', ''),
            request_category=form_data.get('requestCategory', ''),
            grant_code=form_data.get('grantCode', ''),
            project_title=form_data.get('projectTitle', ''),
            plant_species=form_data.get('plantSpecies', ''),
            current_date=current_date,
            start_date=start_date,
            end_date=end_date,
            zone_number=form_data.get('zoneNumber', ''),
            number_of_tables=int(form_data.get('numberOfTables', 0)),
            photoperiod=int(form_data.get('photoperiod', 0)),
            min_temperature=form_data.get('minTemperature', 0),
            bench=form_data.get('radioOption[]', 0),
            requirements_clarification=form_data.get('requirementsClarification', ''),
        )
        # Save the new instance to the database
        research_request.save()
    except Exception as e:
        return JsonResponse({'error': 'error'})
    # Return a success response
    return JsonResponse({'status': 'success', 'message': 'Research request submitted successfully'})


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


def fetch(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('users:login')
    user_id = request.user.id
    research_requests = ResearchRequest.objects.filter(applicant_account_id=user_id).values('id',
                                                                                            'primary_investigator', ''
                                                                                                                    'department',
                                                                                            'start_date',
                                                                                            'end_date', 'bench',
                                                                                            'lab_room_number',
                                                                                            'approved')
    result = []
    for i in list(research_requests):
        try:
            research_request_id = i['id']
            order = Order.objects.get(research_request_id=research_request_id).order_number
            i['order_id'] = f"/download?order_number={order}"
            result.append(i)
        except:
            i['order_id'] = ''
            result.append(i)
    return JsonResponse(list(research_requests), safe=False)


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


def custom_logout_view(request):
    out(request)
    return redirect('users:index')
