from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterUserForm
from .models import Book, Category, SubCategory


def home(request):
    book_qs = Book.objects.all()
    category_qs = Category.objects.all()
    context = {'books': book_qs, 'categories': category_qs}
    return render(request, "home.html", context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'Incorrect credentials!')
    context = {}
    return render(request, "user_login.html", context)


def user_logout(request):
    logout(request)
    return redirect('home')


def user_register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    context = {'form': form}
    return render(request, "user_register.html", context)


def book_add(request):
    context = {}
    return render(request, "book_add.html", context)


def book_get(request, pk):
    book = get_object_or_404(Book, isbn=pk)
    context = {'book': book}
    return render(request, "book_get.html", context)


def book_filter(request):
    qs = Book.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    isbn_exact_query = request.GET.get('isbn_exact')
    title_or_author_query = request.GET.get('title_or_author')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    category = request.GET.get('category')
    subcategory = request.GET.get('subcategory')

    if title_contains_query:
        qs = qs.filter(title__icontains=title_contains_query)

    elif isbn_exact_query:
        qs = qs.filter(isbn=isbn_exact_query)

    elif title_or_author_query:
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__icontains=title_or_author_query)
                       ).distinct()

    if date_min:
        qs = qs.filter(publication_date__gte=date_min)

    if date_max:
        qs = qs.filter(publication_date__lt=date_max)

    if price_min:
        qs = qs.filter(price__gte=price_min)

    if price_max:
        qs = qs.filter(price__lt=price_max)

    if category and category != 'Choose...':
        qs = qs.filter(category__id=category)

    if subcategory and subcategory != 'Choose...':
        qs = qs.filter(subcategory__id=subcategory)

    context = {'queryset': qs, 'categories': categories}
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
