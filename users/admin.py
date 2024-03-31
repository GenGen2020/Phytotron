import os
import string
import random
from decimal import Decimal

from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.core.files import File
from django.core.mail import send_mail
from django.contrib import admin
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from datetime import date, timedelta, datetime
from users.models import CustomUser, ResearchRequest, Order, OrderDetail, Price
from django.urls import reverse
from django.utils.html import format_html

from users.tools import create_pdf_with_image

admin.site.site_title = "Phytotron"
admin.site.site_header = "Phytotron"


class CustomUserAdmin(UserAdmin):
    def send_registration_email(self, user_email):
        subject = 'Congratulations, you have successfully registered your account'
        message = 'Congratulations on successfully registering your account! Please click the following link to log ' \
                  'in: https://127.0.0.1:8000/login '
        from_email = 'hdcyyg@126.com'  # Replace with your 126 email address
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    def approve_users(self, request, queryset):
        queryset.update(approved=1)
        queryset.update(is_active=1)
        for query in queryset:
            self.send_registration_email(query.email)
        messages.success(request, f"Successfully approved  users.")

    def refuse(self, request, queryset):
        queryset.update(approved=2)
        messages.success(request, f"refuse approved  users.")

    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar',)}),
        (None, {'fields': ('personal_signature',)}),
    ) + (
                    (None, {'fields': ('role',)}),
                )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar',)}),
        (None, {'fields': ('personal_signature',)}),
    ) + (
                        (None, {'fields': ('role',)}),
                    )
    list_display = ['email', 'username', 'role', 'is_active', 'queen', 'supervisor', 'approved']  # 在这里添加你想展示的字段
    search_fields = ('approved',)
    actions = [approve_users]  # 添加你定义的动作
    approve_users.type = 'info'


class DateRangeFilter(SimpleListFilter):
    title = _('date range')
    parameter_name = 'date_range'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('past_7_days', _('Past 7 days')),
            ('this_month', _('This Month')),
            # You can add more options here
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            today = date.today()
            return queryset.filter(start_date__lte=today, end_date__gte=today)
        if self.value() == 'past_7_days':
            today = date.today()
            week_ago = today - timedelta(days=7)
            return queryset.filter(start_date__lte=today, end_date__gte=week_ago)
        if self.value() == 'this_month':
            today = date.today()
            start_of_month = today.replace(day=1)
            return queryset.filter(start_date__lte=today, end_date__gte=start_of_month)
        return queryset


def generate_order_number():
    # 生成一个包含数字和小写字母的 18 位随机字符串
    # Current time in milliseconds since epoch
    current_millis = int(datetime.now().timestamp() * 1000)

    # Convert to string and take the last 5 digits
    time_str = str(current_millis)[-5:]

    # Generate a random 3-digit number and convert to string
    random_str = ''.join(random.choices(string.digits, k=6))

    # Combine both strings to form an 8-character order ID
    return time_str + random_str


class ResearchRequestAdmin(admin.ModelAdmin):
    # Fields to be displayed in the admin list view
    list_display = (
        'primary_investigator', 'department', 'start_date', 'end_date', 'lab_room_number', 'bench', 'order_link',
        'approved')
    search_fields = ('primary_investigator', 'approved')
    list_filter = (DateRangeFilter,)

    def order_link(self, obj):
        order = Order.objects.filter(research_request=obj).first()
        if order:
            # 注意替换 'users' 和 'order' 分别为你的应用名称和模型名称的小写形式
            url = reverse('admin:users_order_change', args=[order.pk])
            return format_html('<a href="{}">View Order</a>', url)
        return "No Order"

    order_link.short_description = 'Order'

    def approve_users(self, request, queryset):
        try:
            with transaction.atomic():
                for query in queryset:
                    query.approved = 1
                    query.save()
                    order_number = generate_order_number()  # 生成订单号
                    start_date = query.start_date
                    end_date = query.end_date
                    days = (end_date - start_date).days
                    lab_room_number = query.lab_room_number
                    price_type = Price.objects.get(type=lab_room_number)
                    # 根据 type 查询对应的价格
                    if query.applicant_account.queen == 0:
                        price = price_type.external_price
                    else:
                        price = price_type.price
                    order = Order.objects.create(
                        order_number=order_number,
                        research_request=query,
                        date=date.today(),
                        basic_billing_fee=price * days,
                        total_amount=price * days
                    )
        except Exception as e:
            messages.error(request, f"An error occurred: {e}. Changes have been rolled back.")
            return

        messages.success(request, f"Successfully approved users and created orders.")

    def refuse(self, request, queryset):
        queryset.update(approved=2)
        messages.success(request, f"refuse approved  users.")

    # def Discount(self, request, queryset):
    #     for query in  queryset:
    #         price = query.price
    #         cut = 0.3
    #         queryset.update(price=price*Decimal(str(cut)))
    #     messages.success(request, f"Discounted successfully.")

    actions = [approve_users, refuse]  # 添加你定义的动作
    approve_users.type = 'success'
    refuse.type = 'danger'
    # Discount.type = 'info'


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1  # 默认显示一个 OrderDetail
    can_delete = True  # 确保可以删除


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display = ['order_number', 'research_request', 'date', 'total_amount']

    def generate_pdf_for_order(self, request, queryset):
        try:
            for query in queryset:
                order_id = query.order_number
                order = Order.objects.get(pk=order_id)
                # 构建PDF内容
                image_path = 'D:\\chatgpt\\Phytotron-main\\users\\static\\image\\logo.jpg'  # 示例图像路径
                days = (order.research_request.end_date - order.research_request.start_date).days
                projectName = Price.objects.get(type=order.research_request.lab_room_number)
                if order.research_request.applicant_account.is_queen == 1:
                    price = projectName.price
                else:
                    price = projectName.external_price
                basic_billing_fee = order.basic_billing_fee
                order_details = OrderDetail.objects.filter(order=order)
                other = "(-15%)" if query.is_discounted is True else ""
                order_details = [
                    {"Description": i.type + other , "Quantity": 1, "Unit Price": i.price, "Amount": i.price, "Tax Code": "HST"}
                    for
                    i in order_details]
                orders_price = order.total_amount - order.basic_billing_fee
                items_list = [
                                 {"Description": f"{order.research_request.lab_room_number}", "Quantity": str(days),
                                  "Unit Price": price,
                                  "Amount": basic_billing_fee,
                                  "Tax Code": "HST"},
                             ] + order_details
                financial_summary = {
                    "basic": str(basic_billing_fee),
                    "Other Taxes": str(orders_price),
                    "Amount Due": str(order.total_amount)
                }
                invoice_info = {
                    "Invoice No": order.order_number,
                    "Customer ID": order.research_request.applicant_account.id,
                    "Invoice Date": order.date,
                    "Payment Terms": "Due upon receipt",
                    "Currency": "USD"
                }
                bill_to_info = [
                    "Performance Plants Inc.",
                    "Jean Hamilton-Varey",
                    "1287 Gardiners Rd. #2",
                    "Kingston ON K7P 3J6",
                    "Canada"
                ]

                # PDF文件的保存路径
                pdf_filename = f'order_{order.order_number}.pdf'
                pdf_path = os.path.join(settings.MEDIA_ROOT, 'users/static/pdfs/', pdf_filename)

                # 生成PDF
                create_pdf_with_image(pdf_path, image_path, items_list, financial_summary, invoice_info, bill_to_info)
                # 更新Order模型的attachment字段
                with open(pdf_path, 'rb') as pdf_file:
                    order.attachment.save(pdf_filename, File(pdf_file), save=True)
                messages.success(request, f"PDF for order {order.order_number} generated and saved.")
        except Order.DoesNotExist:
            messages.error(request, "Order not found.")

    def discount(self, request, queryset):
        for query in queryset:
            if query.is_discounted is False:
                basic_price = query.basic_billing_fee * Decimal('0.85')
                total_price = query.total_amount - query.basic_billing_fee + basic_price
                query.total_amount = total_price
                query.is_discounted = True
                query.save()
        messages.success(request, f"discounted successfully")

    actions = [generate_pdf_for_order, discount]  # 添加你定义的动作
    generate_pdf_for_order.type = 'info'
    discount.type = 'success'

    def save_formset(self, request, form, formset, change):
        # Get new and updated instances
        instances = formset.save(commit=False)
        # Initialize or retrieve the total amount from the Order instance
        total_amount = form.instance.total_amount

        # Update total_amount for each new or updated instance
        for instance in instances:
            # Assuming `price` field exists in `OrderDetail` and relates to a `Price` model with a `price` attribute
            total_amount += instance.price.price
            instance.save()

        # Deduct total_amount for each deleted instance
        for instance in formset.deleted_objects:
            total_amount -= instance.price.price
            instance.delete()  # Explicitly delete the instance

        # Update the total amount on the Order instance
        form.instance.total_amount = total_amount
        form.instance.save()

        # Save many-to-many data for the formset
        formset.save_m2m()


admin.site.register(Price)
admin.site.register(ResearchRequest, ResearchRequestAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
