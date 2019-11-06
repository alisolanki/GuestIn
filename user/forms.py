from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Userregister(UserCreationForm):
    Email = forms.EmailField()
    class meta:
        model = User
        fields = ['username','Email','password1','password2']