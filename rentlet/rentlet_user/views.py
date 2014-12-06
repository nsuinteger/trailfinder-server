from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from jsonutil import json_success, json_fail
from rentlet_user.models import RentletUser


def isAuthenticate(username, password):
    #Todo isAuthenticate
    user_list = RentletUser.objects.all()
    for user in user_list:
        if user.username == username and user.password == password:
            return True
    return False


def user_login(request):
    return json_success(request, "login success")
    try:
        username = request.POST['username']
        password = request.POST['password']
        if (isAuthenticate(username, password)):
            return json_success(request, "login successfully")
    except KeyError:
        return json_fail(request, "login fail")
