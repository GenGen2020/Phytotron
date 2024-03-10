from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    ROLE = (
        (0, "student"),
        (1, "professor"),
        (2, "company")
    )
    APPROVED = (
        (0, "pending"),
        (1, "approved"),
        (2, "declined")
    )
    role = models.IntegerField(choices=ROLE, default=0, verbose_name='role')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='is_active')
    approved = models.IntegerField(choices=APPROVED, default=0, verbose_name='approve status')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'account management'
        verbose_name = 'account management'
        app_label = 'users'
