from django.forms import ModelForm
from .models import RequestBook


class RequestBookForm(ModelForm):
    class Meta:
        model = RequestBook
        fields = [
           'name',
            'bookName',
            'email'
        ]
