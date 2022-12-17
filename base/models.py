from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Django's User model has limited functionality. Can't add in bio, profile picture, etc.
# Can add a custom user's model using Profile model with one-to-one relation with model attributes
# Another way: Override the User model to create a custom model

class User(AbstractUser):
    pass

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # need to specify related_name bcz User model already connected to host field
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        # changes how data is ordered. adding a '-' makes the order descending
        ordering = ['-updated', '-created']


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated', '-created']

# create super-user to access the django admin page # python manage.py createsuperuser
# user: savio49
# password: P@ssw0rd@1234
