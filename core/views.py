from multiprocessing import context
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    context = {}
    return render(request, "home.html", context)


def user_login(request):
    context = {}
    return render(request, "user_login.html", context)


def user_logout(request):
    context = {}
    return redirect('home')


def user_register(request):
    context = {}
    return render(request, "user_register.html", context)


def book_add(request):
    context = {}
    return render(request, "book_add.html", context)


def book_get(request, pk):
    context = {}
    return render(request, "book_get.html", context)


def book_filter(request):
    context = {}
    return render(request, "book_filter.html", context)


def cart_get(request):
    context = {}
    return render(request, "cart_get.html", context)


def cart_add(request):
    context = {}
    return render(request, "cart_get.html", context)


def cart_subtract(request):
    context = {}
    return render(request, "cart_get.html", context)
