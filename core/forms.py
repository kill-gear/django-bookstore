from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Book


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookAddForm(ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'category', 'subcategory',
                  'author', 'publisher', 'publication_date', 'image_url', 'price', 'about']
