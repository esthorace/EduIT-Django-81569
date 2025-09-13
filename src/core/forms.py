from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
