from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import MainMenu
from .models import Book

# send_mail used for messaging capabilities.
from django.core.mail import send_mail

# Use User auth table for username info
from django.contrib.auth.models import User


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


# Contact function used to send message.
def contact(request):
    if request.method == "POST":
        # Fields to be collected for message
        post_username = request.POST['post-username']
        message_book = request.POST['message-book']
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Obtain email of post user from auth table
        user = User.objects.get(username=post_username)
        user_email = user.email

        # Send email
        send_mail(
            'Re: ' + message_book + ', Message from ' + message_name,
            message,
            message_email,
            [user_email],
            )
        return render(request, 'bookMng/book_detail.html', {'message_name': message_name})
    else:
        return render(request, 'bookMng/book_detail.html', {})
