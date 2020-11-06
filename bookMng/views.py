from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import MainMenu
from .models import Book


# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'bookMng/home.html',{
        'item_list': MainMenu.objects.all()
    })


def home(request):
    return render(request, 'home.html')


def displaybooks(request):
    books = Book.objects.all()
    for b in books:
            b.pic_path = b.picture.url[14:]
            return render (request, 'bookMng/displaybooks.html', {
                'item_link': MainMenu.objects.all(), 'books': books
            })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
            'form': form
    })
