from django.shortcuts import render


def login(request):
    return render(request, 'store/authentication/login.html', locals())


def register(request):
    pass


def logout(request):
    pass