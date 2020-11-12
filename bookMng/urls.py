from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('displaybooks', views.displaybooks, name='displaybooks')
    # urlpattern for contact form.
    path('book_detail', views.contact, name="contact"),
]