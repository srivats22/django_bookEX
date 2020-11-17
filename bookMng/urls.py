from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('requestbook', views.requestbook, name='requestbook'),
    path('displayrequest', views.requestedbooks, name='requestedbooks'),
    path('displayrequest', views.requestedbooks, name='requestedbooks')
    # # urlpattern for contact form.
    # path('book_detail', views.contact, name="contact"),
]