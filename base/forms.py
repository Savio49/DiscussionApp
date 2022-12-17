from django.forms import ModelForm
from .models import Room, User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # or specify a list of attributes of Room in a list. Eg. ['name', 'description'] or use exclude field in the same manner
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'bio', 'avatar']
