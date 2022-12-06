from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class name = Database name
# attributes of class = columns of database
# every instance of class = row of database

# default models of django are mentioned in settings.py
# set them up using # python manage.py migrate


# Topics are super-fields of Rooms, i.e. each room has only one topic, but a topic can have multiple rooms.
class Topic(models.Model):
    # Place it above Room model in order to access it in Room
    name = models.CharField(max_length=200)

    def __string__(self):
        return self.name


class Room(models.Model):
    # host
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null=True means description can be blank, blank=True means when form is saved, this field can be empty
    description = models.TextField(null=True, blank=True)
    # participants =
    # takes time snapshot of anytime this model instance was updated i.e whenever the save method was run to update this model. auto_now means Django automatically takes a time stamp when save method is run
    updated = models.DateTimeField(auto_now=True)
    # takes snapshot only the first time when model was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    # django already has a built in user-model. User can have many messages, but each message has only one user. When a user is deleted, the messages are deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # one to many relationship: a user can have many messages. Foreign key in databases. CASCADE deletes all the messages in the room if the room is deleted. SET_NULL sets the message values to null on room deletion
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


# models are classes which make up the database
# migration means converting a model into a database
# prepare migrations using: # python manage.py makemigrations
# migrate using: # python manage.py migrate
# access the database using either third party software like sqlitestudio or django built-in admin portal
# create super-user to access the django admin page # python manage.py createsuperuser
# user: savio49
# password: P@ssw0rd@1234
