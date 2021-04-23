import os
import uuid

from django.db import models
from uuid import uuid4
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    order_category = models.IntegerField()
    description = models.CharField(max_length=400, null=True)
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {self.order_category}'


class Service(models.Model):
    def get_file_name_service(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/service/', filename)

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=400, null=True)
    photo = models.ImageField(upload_to=get_file_name_service)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} : {self.category}'


class Events(models.Model):
    def get_file_name_events(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/events/', filename)

    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to=get_file_name_events)
    event_date = models.DateField()
    event_time = models.TimeField()

    def __str__(self):
        return f'{self.title}'


class UserMessages(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    message = models.CharField(max_length=200)

    is_checked = models.BooleanField(default=False)
    send_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.user_email}'
