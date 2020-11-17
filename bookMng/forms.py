from django.forms import ModelForm
from .models import Book, RequestBook


class RequestBookForm(ModelForm):
    class Meta:
        model = RequestBook
        fields = [
           'name',
            'bookName',
            'email'
        ]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]