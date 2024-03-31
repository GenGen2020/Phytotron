# Generated by Django 5.0.1 on 2024-03-13 09:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_researchrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'student'), (1, 'professor'), (2, 'company'), (3, 'admin')], default=0, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='researchrequest',
            name='applicant_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='research_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
