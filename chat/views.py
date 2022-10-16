import logging
from django.shortcuts import render, redirect
from django.views import View
from .models import Profile, Chats
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

logging.basicConfig(filename='user_logs.log', encoding='utf-8', level=logging.DEBUG)

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    chats = Chats.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user_name': request.user.username,
        'chats': chats
    })


class Registration(View):

    def post(self, request):
        try:
            Profile.objects.create_user(username=request.POST.get("username"), password=request.POST.get("password"))
            return redirect('login')
        except Exception as e:
            logging.exception(e)
            return render(request, "chat/registration.html")

    def get(self, request):
        return render(request, "chat/registration.html")


class Login(View):

    def post(self, request):
        try:
            user_name = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if not user_name:
                return render(request, "chat/login.html")
            login(request, user_name)
            return redirect('index')
        except Exception as e:
            logging.exception(e)
            return render(request, "chat/login.html")

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, "chat/login.html")


class UserLogout(View):
    """
    This class logout the user from profile page
    """
    def get(self, request):
        logout(request)
        return redirect('login')