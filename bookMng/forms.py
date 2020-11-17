from django.forms import ModelForm
from .models import Book, RequestBook
from .models import Review


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

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating',
            'title',
            'description',
        ]
