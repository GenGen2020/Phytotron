from django.shortcuts import render
from django.http import HttpRequest
from hotel import models

# Create your views here.
def index(request: HttpRequest):
    res = {}
    hotels = models.HotelModel.objects.all()
    for hotel in hotels:
        rooms = models.RoomModel.objects.filter(refer_hotel=hotel)
        data = [i.room_id for i in rooms]
        data.sort()
        res[hotel.hotel_name] = data
    print(res)
    return render(request=request,
                  template_name='index.html',
                  context={"hotels": res},
                  )

def rooms(request: HttpRequest, hotel: str, room_id: str):
    data = {"status": False,
            "error": "",
            "msg": ""}
    obj = models.RoomModel.objects.filter(refer_hotel=hotel, room_id=room_id).first()
    if obj is None:
        data['error'] = "error hotel or room id"
    else:
        data['status'] = not obj.used
        if not obj.used:
            data['msg'] = "this room is open for user"
        else:
            data['msg'] = "this room is closed"
    return render(request=request,
                  template_name="rooms.html",
                  context={
                      "hotel": hotel,
                      "room_id": room_id,
                      "data": data,
                    },
                )