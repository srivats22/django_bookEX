from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('requestbook', views.requestbook, name='requestbook'),
    path('displayrequest', views.requestedbooks, name='requestedbooks')
    # urlpattern for contact form.
    path('book_detail', views.contact, name="contact"),
]