from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    publish_date = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False)
    user_name = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class RequestBook(models.Model):
    name = models.CharField(max_length=200)
    bookName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
