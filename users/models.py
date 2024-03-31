from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from users.validate import validate_file_extension


class CustomUser(AbstractUser):
    ROLE = (
        (0, "student"),
        (1, "professor"),
        (2, "company"),
        (3, "admin"),
    )
    APPROVED = (
        (0, "pending"),
        (1, "approved"),
        (2, "declined")
    )
    is_queen = (
        (0, "no"),
        (1, "yes"),
    )

    role = models.IntegerField(choices=ROLE, default=0, verbose_name='role')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='is_active')
    approved = models.IntegerField(choices=APPROVED, default=0, verbose_name='approve status')
    avatar = models.ImageField(upload_to='users/static/avatars/', null=True, blank=True,
                               default="users/static/avatars/photo-1587822463356-cd0b11a919ae.jpg")
    personal_signature = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    supervisor = models.CharField(max_length=255, default='')
    queen = models.IntegerField(choices=is_queen, default=0, verbose_name='queen')
    review_file = models.FileField(upload_to='users/static/files/', null=True, blank=True, validators=[validate_file_extension])

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'account management'
        verbose_name = 'account management'
        app_label = 'users'


class ResearchRequest(models.Model):
    # 外键，关联到自定义用户模型
    applicant_account = models.ForeignKey(
        CustomUser,  # 使用项目的用户模型
        on_delete=models.CASCADE,  # 当关联的用户被删除时，也删除这个研究请求
        related_name='research_requests',  # 为反向查询定义一个名字
    )
    # 主要研究员
    primary_investigator = models.CharField(max_length=255)
    # 主要联系人
    primary_contact = models.CharField(max_length=255)
    # 部门或外部公司
    department = models.CharField(max_length=255)
    # 实验室房间号或外部地址
    lab_room_number = models.CharField(max_length=255)
    # 工作联系电话
    contact_phone = models.CharField(max_length=255)
    # 非工作时间联系电话
    contact_after_hours = models.CharField(max_length=255)
    # 电子邮件地址
    email = models.EmailField()
    # 请求分类
    request_category = models.CharField(max_length=255)
    # CFOAPAL或资助代码或课程代码
    grant_code = models.CharField(max_length=255)
    # 项目标题 - 简要描述
    project_title = models.CharField(max_length=255)
    # 植物种类
    plant_species = models.CharField(max_length=255)
    # 动物护理或安全问题
    safety_concern = models.BooleanField(default=False)
    # 当前日期
    current_date = models.DateField()
    # 期望开始日期
    start_date = models.DateField()
    # 期望结束日期
    end_date = models.DateField()
    # 希望的区号
    zone_number = models.CharField(max_length=255)
    # 桌子数量
    number_of_tables = models.IntegerField()
    # 光照周期（小时）
    photoperiod = models.IntegerField()
    # 最低温度（°C）
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    # 特殊要求说明
    requirements_clarification = models.TextField()

    bench = models.CharField(max_length=255, default='')

    is_active = models.BooleanField(default=True, verbose_name='Animal Care')

    APPROVED = (
        (0, "pending"),
        (1, "approved"),
        (2, "declined")
    )

    approved = models.IntegerField(choices=APPROVED, default=0, verbose_name='approve status')

    def __str__(self):
        return self.project_title


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    external_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"Price: {self.price}, External Price: {self.external_price}, Type: {self.type}"


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    research_request = models.ForeignKey(ResearchRequest, on_delete=models.CASCADE, related_name='orders')
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    basic_billing_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    attachment = models.FileField(upload_to='users/static/pdfs/', null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)  # Indicates if the order has a discount applied

    def __str__(self):
        return f"Order Number: {self.order_number}, Date: {self.date}, Total Amount: {self.total_amount}"



class OrderDetail(models.Model):
    detail_number = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    # 通过外键关联到 Price 模型
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    # 通过外键关联到 Price 模型的类型字段
    type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Detail Number: {self.detail_number}, Price: {self.price.price}, Type: {self.type}"
