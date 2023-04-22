from django.shortcuts import render


def login(request):
    return render(request, 'store/auth/login.html', locals())


def register(request):
    pass


def logout(request):
    pass