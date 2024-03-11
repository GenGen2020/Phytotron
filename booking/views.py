from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Booking, Facility, User
from django.utils.dateparse import parse_date

def index(request):
    return render(request, 'booking/index.html')

def check_availability(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    #测试用，实际需遍历所有bookings，找到start_date没有被预定的设施id并返还给前端
    availability_start_date = start_date not in ['2024-04-10', '2024-04-11']
    availability_end_date = end_date not in ['2024-04-10', '2024-04-11']
    return JsonResponse({
        'availability_start_date': availability_start_date,
        'availability_end_date': availability_end_date
    })


def submit_booking(request):
        if request.method == 'POST':
            facility_id = request.POST.get('facility_id')  # Get the facility_id from the form
            type = request.POST.get('facility_type')
            facility = Facility.objects.get(id=facility_id)  # Fetch the Facility object


            #在没有用户时创建用户测试：
            name = 'test1'  # 假设你的表单里有name字段
            email = 'test@test.com'  # 假设你的表单里有email字段
            user, created = User.objects.get_or_create(email=email, defaults={'name': name})

        # 捕获表单数据
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            hours_light = request.POST.get('hours_light')
            hours_dark = request.POST.get('hours_dark')
            temp_light = request.POST.get('temp_light')
            temp_dark = request.POST.get('temp_dark')
            humidity_light = request.POST.get('humidity_light')
            humidity_dark = request.POST.get('humidity_dark')
            light_level = request.POST.get('light_level')

        # 创建并保存新的Booking对象
            new_booking = Booking.objects.create(
                user = user,
                facility=facility,
                start_date=start_date,
                end_date=end_date,
                hours_light=hours_light,
                hours_dark=hours_dark,
                temp_light=temp_light,
                temp_dark=temp_dark,
                humidity_light=humidity_light,
                humidity_dark=humidity_dark,
                light_level=light_level
            )

        # 可以重定向到一个新的URL，或者返回一个确认页面
            return redirect('check_availability')  # 这里要修改，返回到主页
        else:
        # 如果不是POST请求，重定向到表单页面或其他适当页面
            return redirect('index')  # 返回到表单页面