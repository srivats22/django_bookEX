from .models import MainMenu
from .models import Book, RequestBook
from .forms import RequestBookForm
from .forms import BookForm
from .forms import ReviewForm
from .forms import SearchForm

from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    form = SearchForm()
    books = book_search(request)
    try:
        for b in books:
            b.pic_path = b.picture.url[19:]
    except Exception:
        return HttpResponseRedirect('/displaybooks')
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'form': form
                  })


@login_required(login_url=reverse_lazy('login'))
def book_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data['name']
            books = Book.objects.filter(name__icontains=data)
            return books
    else:
        return Book.objects.all()


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(user_name=request.user)
    for b in books:
        b.pic_path = b.picture.url[19:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[19:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })

@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            try:
                book.user_name = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


def requestedbooks(request):
    requestbooks = RequestBook.objects.all()
    for rb in requestbooks:
        return render(request, 'bookMng/displayrequest.html', {
            'requestedbooks': requestbooks
        })


def requestbook(request):
    submitted = False
    if request.method == 'POST':
        form = RequestBookForm(
            request.POST
        )
        if form.is_valid():
            request_book = form.save(commit=False)
            request_book.save()
            return HttpResponseRedirect('/requestbook?submitted=True')
    else:
        form = RequestBookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'bookMng/requestbook.html',
        {
            'form': form,
            'submitted': submitted
        }
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
            'form': form
    })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[19:]
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            if 1 <= review.rating <= 5:
                try:
                    review.book = book
                    review.username = request.user
                except Exception:
                    pass
                review.save()
            return HttpResponseRedirect(f'/book_detail/{book_id}')
    else:
        form = ReviewForm()
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'book': book
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

        # Message composition for email
        send_mail(
            'Re: ' + message_book + ', Message from ' + message_name,
            message,
            message_email,
            [user_email],
            )
        return render(request, 'bookMng/book_detail.html', {'message_name': message_name})
    else:
        return render(request, 'bookMng/book_detail.html', {})