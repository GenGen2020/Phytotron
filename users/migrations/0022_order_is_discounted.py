# Generated by Django 5.0.1 on 2024-03-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_customuser_review_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_discounted',
            field=models.BooleanField(default=False),
        ),
    ]