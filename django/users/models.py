from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def __self__(self):
            return self.model.username