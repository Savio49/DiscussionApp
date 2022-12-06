from django.contrib import admin

# Register your models here.
# To view models on the admin page, register your models

# User model already registered by default
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
