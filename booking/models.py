from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()

class Facility(models.Model):
    FACILITY_TYPE_CHOICES = [
        ('greenhouse', 'Greenhouse Zone'),
        ('chamber', 'Growth Chamber')
    ]
    facility_type = models.CharField(max_length=10, choices=FACILITY_TYPE_CHOICES)
    status = models.CharField(max_length=100)

class Booking(models.Model):
    FACILITY_TYPE_CHOICES = [
        ('greenhouse', 'Greenhouse Zone'),
        ('chamber', 'Growth Chamber')
    ]
    facility_type = models.CharField(max_length=10, choices=FACILITY_TYPE_CHOICES)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    hours_light = models.IntegerField()
    hours_dark = models.IntegerField()
    temp_light = models.FloatField()
    temp_dark = models.FloatField()
    humidity_light = models.FloatField()
    humidity_dark = models.FloatField()
    light_level = models.IntegerField()
    status = models.CharField(max_length=100)

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

