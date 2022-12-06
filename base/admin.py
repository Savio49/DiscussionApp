from django.contrib import admin

# Register your models here.
# To view models on the admin page, register your models

from .models import Room

admin.site.register(Room)
