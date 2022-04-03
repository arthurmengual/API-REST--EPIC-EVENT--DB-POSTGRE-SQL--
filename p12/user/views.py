from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect()
    else:
        return redirect()


def logout_view(request):
    logout(request)
    return redirect()
