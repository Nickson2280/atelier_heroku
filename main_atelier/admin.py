from django.contrib import admin
from .models import Category, Service, Events, UserMessages

# Register your models here.
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Events)
admin.site.register(UserMessages)
