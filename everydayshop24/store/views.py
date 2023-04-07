from django.shortcuts import render
from .forms import CustomerForm


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def login(request):
    name = 'NameName'
    form = CustomerForm(request.POST or None)

    return render(request, 'store/login.html', locals())