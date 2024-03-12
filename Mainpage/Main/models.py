from django.db import models

# Create your models here.
class HotelModel(models.Model):
    hotel_name = models.CharField(max_length=128, verbose_name="酒店名", unique=True)

class RoomModel(models.Model):
    room_id = models.IntegerField(verbose_name="酒店房间号")
    refer_hotel = models.ForeignKey(to=HotelModel, to_field="hotel_name", on_delete=models.CASCADE)
    used = models.BooleanField(default=False, verbose_name="酒店是否可预定")

