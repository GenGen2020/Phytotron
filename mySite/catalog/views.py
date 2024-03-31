from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def mainPage(request):
    return render(request, 'mainPage.html')

def reservation(request):
    return render(request, 'reservation.html')
